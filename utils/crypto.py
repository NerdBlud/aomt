from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_data(data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded_data = data + (16 - len(data) % 16) * " "  # Padding to 16 bytes
    encrypted = cipher.encrypt(padded_data.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_data(encrypted_data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_data))
    return decrypted.decode('utf-8').strip()

def generate_key():
    return base64.b64encode(get_random_bytes(16)).decode('utf-8')