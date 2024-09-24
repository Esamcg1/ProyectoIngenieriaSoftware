# import hashlib
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# import os

# # Función para cifrar con AES-256
# def encrypt_aes256(text, key):
#     # Asegurarse de que la clave tenga exactamente 32 bytes (256 bits)
#     key = key.ljust(32)[:32].encode('utf-8')
#     iv = os.urandom(16)  # Vector de inicialización (16 bytes)
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     encryptor = cipher.encryptor()
#     encrypted = encryptor.update(text.encode('utf-8')) + encryptor.finalize()
#     return iv + encrypted  # Se regresa el IV junto con el texto cifrado

# # Función para generar hash MD5
# def generate_md5(text):
#     return hashlib.md5(text.encode('utf-8')).hexdigest()

# # Función para generar hash SHA-256
# def generate_sha256(text):
#     return hashlib.sha256(text.encode('utf-8')).hexdigest()

# # Función para solicitar al usuario el algoritmo a usar
# def select_algorithm():
#     print("Seleccione el algoritmo de cifrado:")
#     print("1. MD5 (Hash)")
#     print("2. SHA-256 (Hash)")
#     print("3. AES-256 (Cifrado simétrico)")
#     choice = input("Ingrese el número correspondiente al algoritmo deseado: ")
#     return choice

# # Función principal del flujo del sistema
# def main():
#     # Solicitar palabra o cadena de caracteres al usuario
#     text = input("Ingrese la palabra o cadena de caracteres que desea cifrar: ")

#     # Solicitar el tipo de algoritmo a usar
#     choice = select_algorithm()

#     if choice == '1':
#         # Generar y mostrar el hash MD5
#         hashed_value = generate_md5(text)
#         print(f"MD5 Hash: {hashed_value}")
#     elif choice == '2':
#         # Generar y mostrar el hash SHA-256
#         hashed_value = generate_sha256(text)
#         print(f"SHA-256 Hash: {hashed_value}")
#     elif choice == '3':
#         # Generar una clave para AES-256
#         key = input("Ingrese una clave para el cifrado (se truncará o ajustará a 32 caracteres si es necesario): ")
#         encrypted_value = encrypt_aes256(text, key)
#         print(f"Texto cifrado con AES-256: {encrypted_value.hex()}")
#         print(f"Clave para descifrar: {key}")
#     else:
#         print("Algoritmo no válido. Intente de nuevo.")

# # Comprobar si el script se está ejecutando directamente
# if __name__ == '__main__':
#     main()


import os
from logica import (encrypt_aes256, decrypt_aes256, encrypt_blowfish, decrypt_blowfish,
                              encrypt_3des, decrypt_3des, generate_md5, generate_sha256)

def select_algorithm():
    print("\nSeleccione el algoritmo de cifrado:")
    print("1. MD5 (Hash)")
    print("2. SHA-256 (Hash)")
    print("3. AES-256 (Cifrado/Descifrado simétrico)")
    print("4. Blowfish (Cifrado/Descifrado simétrico)")
    print("5. Triple DES (Cifrado/Descifrado simétrico)")
    choice = input("Ingrese el número correspondiente al algoritmo deseado: ")
    return choice

# Metodo para el cifrado
def handle_encryption():
    text = input("\nIngrese la palabra o cadena de caracteres que desea cifrar: ")
    choice = select_algorithm()

    if choice == '1':
        print(f"MD5 Hash: {generate_md5(text)}")
    elif choice == '2':
        print(f"SHA-256 Hash: {generate_sha256(text)}")
    elif choice in ['3', '4', '5']:
        key = input("Ingrese una clave para el cifrado o presione Enter para generar una automáticamente: ")
        if not key:
            key = os.urandom(16).hex()  # Generar una clave aleatoria si no se proporciona
            print(f"Clave generada automáticamente: {key}")

        if choice == '3':
            encrypted_value = encrypt_aes256(text, key)
            print(f"Texto cifrado con AES-256: {encrypted_value}")
            print(f"Clave para descifrar: {key}")
        elif choice == '4':
            encrypted_value = encrypt_blowfish(text, key)
            print(f"Texto cifrado con Blowfish: {encrypted_value}")
            print(f"Clave para descifrar: {key}")
        elif choice == '5':
            encrypted_value = encrypt_3des(text, key)
            print(f"Texto cifrado con Triple DES: {encrypted_value}")
            print(f"Clave para descifrar: {key}")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

# Manejar el descifrado
def handle_decryption():
    encrypted_text = input("\nIngrese el texto cifrado que desea descifrar: ")
    key = input("Ingrese la clave utilizada para cifrar: ")
    choice = select_algorithm()

    try:
        if choice == '3':
            decrypted_value = decrypt_aes256(encrypted_text, key)
            print(f"Texto descifrado con AES-256: {decrypted_value}")
        elif choice == '4':
            decrypted_value = decrypt_blowfish(encrypted_text, key)
            print(f"Texto descifrado con Blowfish: {decrypted_value}")
        elif choice == '5':
            decrypted_value = decrypt_3des(encrypted_text, key)
            print(f"Texto descifrado con Triple DES: {decrypted_value}")
        else:
            print("Opción no válida para descifrar.")
    except Exception as e:
        print(f"Error durante el descifrado: {e}")

# Función principal del sistema
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Cifrar un texto")
        print("2. Descifrar un texto")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            handle_encryption()
        elif choice == '2':
            handle_decryption()
        elif choice == '3':
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecucion del Script
if __name__ == '__main__':
    main()



