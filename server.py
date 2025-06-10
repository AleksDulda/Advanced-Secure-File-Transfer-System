import socket
from pathlib import Path
from crypto_utils import generate_rsa_keys, decrypt_rsa, decrypt_aes
import hashlib
import traceback

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5001
CHUNK_SIZE = 1024

def recv_all(conn, total_len):
    data = b""
    while len(data) < total_len:
        part = conn.recv(min(CHUNK_SIZE, total_len - len(data)))
        if not part:
            raise ConnectionError("Veri akışı kesildi.")
        data += part
    return data

def run_server():
    try:
        # 🔐 RSA anahtarları oluşturuluyor
        print("[🔐] RSA-2048 anahtar çifti oluşturuluyor...")
        private_key, public_key = generate_rsa_keys()

        s = socket.socket()
        s.bind((SERVER_IP, SERVER_PORT))
        s.listen(1)
        print(f"[+] Sunucu dinleniyor: {SERVER_IP}:{SERVER_PORT}")

        conn, addr = s.accept()
        print(f"[+] Bağlantı alındı: {addr}")

        # 📨 RSA public key istemciye gönderiliyor
        print("[📤] RSA public key istemciye gönderiliyor...")
        conn.sendall(public_key)

        # 🛡️ AES anahtarı alınıyor
        print("[📥] RSA ile şifrelenmiş AES-128 anahtarı alınıyor...")
        key_len = int.from_bytes(conn.recv(4), 'big')
        encrypted_key = conn.recv(key_len)
        aes_key = decrypt_rsa(encrypted_key, private_key)
        print("[🔓] AES anahtarı başarıyla çözüldü.")

        # 🧩 Şifreli veri parçalar halinde alınıyor
        print("[📥] Dosya verisi parçalara ayrılmış şekilde alınıyor...")
        data_len = int.from_bytes(conn.recv(8), 'big')
        encrypted_data = recv_all(conn, data_len)
        print(f"[📦] {data_len} baytlık şifreli veri alındı.")

        # 🧾 SHA-256 hash alınıyor
        print("[🔎] Dosya bütünlük doğrulama SHA-256 hash değeri alınıyor...")
        expected_hash = recv_all(conn, 32)

        # 🔓 AES ile veri çözülüyor
        print("[🔓] AES-128 ile dosya çözülüyor...")
        decrypted_data = decrypt_aes(encrypted_data, aes_key)

        # ✅ Checksum kontrolü
        actual_hash = hashlib.sha256(decrypted_data).digest()
        if actual_hash != expected_hash:
            print("[❗] Checksum uyuşmazlığı: Dosya bozulmuş olabilir.")
        else:
            print("[✅] Checksum doğrulandı. Dosya bütünlüğü sağlandı.")

        # 💾 Dosya kaydediliyor
        Path("received_file.txt").write_bytes(decrypted_data)
        print("[💾] Dosya başarıyla 'received_file.txt' olarak kaydedildi.")

    except Exception as e:
        print("[💥] Hata oluştu:")
        traceback.print_exc()

if __name__ == "__main__":
    run_server()
