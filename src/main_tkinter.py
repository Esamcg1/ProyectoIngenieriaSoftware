import os
import tkinter as tk
from tkinter import messagebox
from styles import styles
from conexion.conexion import obtener_conexion
from logica import (encrypt_aes256, decrypt_aes256, encrypt_blowfish, decrypt_blowfish,
                    encrypt_3des, decrypt_3des, generate_md5, generate_sha256)

def encrypt_text(text_entry, key_entry, algorithm_var):
    text = text_entry.get()
    key = key_entry.get()
    algorithm_name = algorithm_var.get()  # Cambiado a algorithm_name para diferenciarlo del ID

    if not text:
        messagebox.showerror("Error", "Por favor ingrese un texto.")
        return

    # Conexión a la base de datos
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Obtener el id_algoritmo a partir del nombre del algoritmo
    cursor.execute("SELECT id_algoritmo FROM algoritmos WHERE nombre_algoritmo = ?", (algorithm_name,))
    result = cursor.fetchone()
    if result is None:
        messagebox.showerror("Error", "Algoritmo no encontrado en la base de datos.")
        return

    id_algoritmo = result[0]  # Este es el ID que corresponde al nombre del algoritmo

    # Leer el usuario actual desde el archivo temporal
    try:
        with open("usuario_actual.txt", "r") as file:
            nombre_usuario = file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo de usuario actual.")
        return

    # Obtener el id_usuario a partir del nombre de usuario
    cursor.execute("SELECT id_usuario FROM usuario WHERE nombre = ?", (nombre_usuario,))
    result = cursor.fetchone()
    if result is None:
        messagebox.showerror("Error", "Usuario no encontrado en la base de datos.")
        return

    id_usuario = result[0]  # Este es el ID del usuario

    # Proceso de cifrado
    if algorithm_name == 'MD5':
        result = generate_md5(text)
        messagebox.showinfo("Resultado", f"Algoritmo: {algorithm_name}\nMD5 Hash: {result}")
        encrypted_value = result  # Almacenar el hash como valor cifrado
    elif algorithm_name == 'SHA-256':
        result = generate_sha256(text)
        messagebox.showinfo("Resultado", f"Algoritmo: {algorithm_name}\nSHA-256 Hash: {result}")
        encrypted_value = result
    else:
        if not key:
            key = os.urandom(16).hex()  # Generar una clave aleatoria si no se proporciona
            messagebox.showinfo("Clave generada", f"Clave generada automáticamente: {key}")

        if algorithm_name == 'AES-256':
            encrypted_value = encrypt_aes256(text, key)
        elif algorithm_name == 'Blowfish':
            encrypted_value = encrypt_blowfish(text, key)
        elif algorithm_name == 'Triple DES':
            encrypted_value = encrypt_3des(text, key)

    # Guardar datos en la base de datos
    cursor.execute("""
        INSERT INTO cadenas (texto, clave, id_algoritmo, texto_cifrado, id_usuario)
        VALUES (?, ?, ?, ?, ?)
    """, (text, key, id_algoritmo, encrypted_value, id_usuario))
    
    conn.commit()
    cursor.close()
    conn.close()

        # Mostrar el texto cifrado
    result_window = tk.Toplevel()
    result_window.title("Texto cifrado")
    result_window.configure(bg="#1E1E2E")
    result_window.geometry("450x300")

    # Etiquetas con estilos
    tk.Label(
        result_window, bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style(),
        text=f"Algoritmo utilizado: {algorithm_name}"
    ).pack(pady=5)

    tk.Label(
        result_window, bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style,
        text=f"Texto cifrado:\n{encrypted_value}"
    ).pack(pady=5)

    tk.Label(
        result_window, bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style,
        text=f"Clave utilizada:\n{key}"
    ).pack(pady=5)

    # Botón para copiar el texto cifrado al portapapeles
    def copy_to_clipboard():
        result_window.clipboard_clear()
        result_window.clipboard_append(encrypted_value)
        messagebox.showinfo("Copiado", "Texto cifrado copiado al portapapeles.")

    copy_btn = tk.Button(result_window, text="Copiar texto cifrado", command=copy_to_clipboard)
    styles.style_button_copy_text(copy_btn)  # Aplica el estilo personalizado
    copy_btn.pack(pady=10)

    # Botón para cerrar la ventana secundaria
    close_btn = tk.Button(result_window, text="Cerrar", command=result_window.destroy)
    styles.style_button_close(close_btn)  # Aplica el estilo personalizado
    close_btn.pack(pady=5)

# Función para descifrar texto 
def decrypt_text(text_entry, key_entry, algorithm_var):
    encrypted_text = text_entry.get()
    key = key_entry.get()
    algorithm = algorithm_var.get()
    
    if not encrypted_text or not key:
        messagebox.showerror("Error", "Por favor ingrese el texto cifrado y la clave.")
        return

    try:
        if algorithm == 'AES-256':
            decrypted_value = decrypt_aes256(encrypted_text, key)
        elif algorithm == 'Blowfish':
            decrypted_value = decrypt_blowfish(encrypted_text, key)
        elif algorithm == 'Triple DES':
            decrypted_value = decrypt_3des(encrypted_text, key)

        messagebox.showinfo("Texto descifrado", f"Texto descifrado: {decrypted_value}")
    except Exception as e:
        messagebox.showerror("Error", f"Error durante el descifrado: {e}")

