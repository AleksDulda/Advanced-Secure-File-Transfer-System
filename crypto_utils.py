from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# RSA anahtar çifti oluştur
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA ile AES anahtarını şifrele
def encrypt_rsa(aes_key, public_key_bytes):
    public_key = RSA.import_key(public_key_bytes)
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(aes_key)

# RSA ile AES anahtarını çöz
def decrypt_rsa(ciphertext, private_key_bytes):
    private_key = RSA.import_key(private_key_bytes)
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(ciphertext)

# AES ile veri şifrele (nonce + tag + ciphertext)
def encrypt_aes(data, aes_key):
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext  # 16B + 16B + N

# AES ile veri çöz (nonce, tag ve ciphertext'i ayırarak)
def decrypt_aes(data, aes_key):
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
