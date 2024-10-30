import tkinter as tk
from tkinter import messagebox
import main_tkinter
from styles import styles
# Crear la ventana principal
root = tk.Tk()
root.configure(bg="#2E2E2E")
root.title("Cifrado y Descifrado")
root.geometry("450x490")

# Campo de texto
tk.Label(root, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Texto:").pack(pady=(20, 5))
text_entry = tk.Entry(root, width=40, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
text_entry.pack(pady=5)

# Campo de clave
tk.Label(root, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Clave (opcional):").pack(pady=5)
key_entry = tk.Entry(root, width=40, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
key_entry.pack(pady=5)

# Variable para seleccionar algoritmo
algorithm_var = tk.StringVar(value='AES-256')

# Opción de algoritmo
algorithms = ['MD5', 'SHA-256', 'AES-256', 'Blowfish', 'Triple DES']
tk.Label(root, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Seleccione el algoritmo:").pack(pady=(10, 5))
for algo in algorithms:
    tk.Radiobutton(root, text=algo, 
    variable=algorithm_var, 
    value=algo, 
    bg="#2E2E2E", 
    fg="white", font=("Arial", 10), selectcolor="#C6FF62", 
    activebackground="#2E2E2E", activeforeground="white").pack(anchor=tk.CENTER)


# Botones para cifrar y descifrar
encrypt_btn = tk.Button(root, text="Cifrar", 
                command=lambda: main_tkinter.encrypt_text(text_entry, key_entry, algorithm_var), 
                width=15)
decrypt_btn = tk.Button(root, text="Descifrar",
                command=lambda: main_tkinter.decrypt_text(text_entry, key_entry, algorithm_var), 
                width=15)

styles.style_button(encrypt_btn)
styles.style_button(decrypt_btn)
encrypt_btn.pack(pady=(15, 5))
decrypt_btn.pack(pady=5)

close_btn = tk.Button(root, text="Salir", command=root.destroy, width=15)
styles.style_button_close(close_btn)
close_btn.pack(pady=15)

# Ejecutar la ventana
root.mainloop()