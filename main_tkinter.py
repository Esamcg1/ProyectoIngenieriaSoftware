import os
from logica import (encrypt_aes256, decrypt_aes256, encrypt_blowfish, decrypt_blowfish,
                    encrypt_3des, decrypt_3des, generate_md5, generate_sha256)
import tkinter as tk
from tkinter import messagebox
from styles import styles

def encrypt_text(text_entry, key_entry, algorithm_var):
    text = text_entry.get()
    key = key_entry.get()
    algorithm = algorithm_var.get()
    
    if not text:
        messagebox.showerror("Error", "Por favor ingrese un texto.")
        return

    if algorithm == 'MD5':
        result = generate_md5(text)
        messagebox.showinfo("Resultado", f"Algoritmo: {algorithm}\nMD5 Hash: {result}")
    elif algorithm == 'SHA-256':
        result = generate_sha256(text)
        messagebox.showinfo("Resultado", f"Algoritmo: {algorithm}\nSHA-256 Hash: {result}")
    else:
        if not key:
            key = os.urandom(16).hex()  # Generar una clave aleatoria si no se proporciona
            messagebox.showinfo("Clave generada", f"Clave generada automáticamente: {key}")

        if algorithm == 'AES-256':
            encrypted_value = encrypt_aes256(text, key)
        elif algorithm == 'Blowfish':
            encrypted_value = encrypt_blowfish(text, key)
        elif algorithm == 'Triple DES':
            encrypted_value = encrypt_3des(text, key)

        # Crear una ventana para mostrar el texto cifrado, la clave y el nombre del algoritmo
        result_window = tk.Toplevel()
        result_window.title("Texto cifrado")
        result_window.configure(bg="#2E2E2E")
        result_window.geometry("450x300")
        # Mostrar la información
        tk.Label(result_window, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text=f"Algoritmo utilizado: {algorithm}").pack(pady=5)
        tk.Label(result_window, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text=f"Texto cifrado:\n{encrypted_value}").pack(pady=5)
        tk.Label(result_window, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text=f"Clave utilizada:\n{key}").pack(pady=5)
        
        # Botón para copiar el texto cifrado al portapapeles
        def copy_to_clipboard():
            result_window.clipboard_clear()
            result_window.clipboard_append(encrypted_value)
            messagebox.showinfo("Copiado", "Texto cifrado copiado al portapapeles.")

        copy_btn = tk.Button(result_window, text="Copiar texto cifrado", command=copy_to_clipboard)
        styles.style_button_copy_text(copy_btn)
        copy_btn.pack(pady=10)
        
        # Cerrar la ventana secundaria
        close_btn = tk.Button(result_window, text="Cerrar", command=result_window.destroy)
        styles.style_button_close(close_btn)
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