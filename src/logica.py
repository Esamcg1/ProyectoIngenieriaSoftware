import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
import random
import string
# Función para cifrar con AES-256
def encrypt_aes256(text, key):
    key = key.ljust(32)[:32].encode('utf-8')  # Ajustar la clave a 32 bytes
    iv = os.urandom(16)  # Iniciar el vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
    return base64.b64encode(iv + encrypted).decode('utf-8')

# Función para descifrar con AES-256
def decrypt_aes256(encrypted_text, key):
    key = key.ljust(32)[:32].encode('utf-8')
    encrypted_text = base64.b64decode(encrypted_text.encode('utf-8'))
    iv = encrypted_text[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_text[16:]) + decryptor.finalize()
    return decrypted.decode('utf-8')

# Función para cifrar con Blowfish
def encrypt_blowfish(text, key):
    key = key.ljust(16)[:16].encode('utf-8')  # Blowfish soporta hasta 16 bytes
    iv = os.urandom(8)  # Vector de inicialización (8 bytes)
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
    return base64.b64encode(iv + encrypted).decode('utf-8')

# Función para descifrar con Blowfish
def decrypt_blowfish(encrypted_text, key):
    key = key.ljust(16)[:16].encode('utf-8')
    encrypted_text = base64.b64decode(encrypted_text.encode('utf-8'))
    iv = encrypted_text[:8]
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_text[8:]) + decryptor.finalize()
    return decrypted.decode('utf-8')

# Función para cifrar con Triple DES
def encrypt_3des(text, key):
    key = key.ljust(24)[:24].encode('utf-8')  # Ajustar la clave dada por usuario
    iv = os.urandom(8)  # Iniciar vector
    cipher = Cipher(algorithms.TripleDES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
    return base64.b64encode(iv + encrypted).decode('utf-8')

# Función para descifrar con Triple DES
def decrypt_3des(encrypted_text, key):
    key = key.ljust(24)[:24].encode('utf-8')
    encrypted_text = base64.b64decode(encrypted_text.encode('utf-8'))
    iv = encrypted_text[:8]
    cipher = Cipher(algorithms.TripleDES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_text[8:]) + decryptor.finalize()
    return decrypted.decode('utf-8')

# Función para generar hash MD5
def generate_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Función para generar hash SHA-256
def generate_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


#:)

