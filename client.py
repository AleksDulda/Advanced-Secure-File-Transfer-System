import socket
from pathlib import Path
from crypto_utils import encrypt_rsa, encrypt_aes
from Crypto.Random import get_random_bytes
import hashlib

CHUNK_SIZE = 1024
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5001

def send_file(file_path):
    # 1. RSA public key al
    s = socket.socket()
    s.connect((SERVER_IP, SERVER_PORT))
    public_key = s.recv(4096)

    # 2. AES anahtarı üret
    aes_key = get_random_bytes(16)
    encrypted_aes_key = encrypt_rsa(aes_key, public_key)
    s.sendall(len(encrypted_aes_key).to_bytes(4, 'big'))
    s.sendall(encrypted_aes_key)

    # 3. Dosyayı oku ve AES ile şifrele
    data = Path(file_path).read_bytes()
    encrypted_data = encrypt_aes(data, aes_key)

    # 4. Toplam uzunluğu gönder
    s.sendall(len(encrypted_data).to_bytes(8, 'big'))

    # 5. Veriyi 1024 baytlık parçalarla gönder
    for i in range(0, len(encrypted_data), CHUNK_SIZE):
        chunk = encrypted_data[i:i + CHUNK_SIZE]
        s.sendall(chunk)

    # 6. SHA-256 hash gönder (ham veri üzerinden)
    sha256 = hashlib.sha256(data).digest()
    s.sendall(sha256)

    s.close()
    print("[✅] Parça parça dosya gönderimi tamamlandı.")
