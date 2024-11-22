import tkinter as tk
from styles import styles
from tkinter import messagebox
from conexion.conexion import obtener_conexion
import main_tkinter
import pyperclip
import re
from conexion import consultas
from funciones.funciones import verificar_seguridad, generar_contrasena
import subprocess

# Leer el nombre del usuario del archivo temporal
try:
    with open("usuario_actual.txt", "r") as file:
        nombre_usuario = file.read()
except FileNotFoundError:
    nombre_usuario = "Usuario"

# Crear la ventana principal
root = tk.Tk()
root.configure(bg="#1E1E2E")
root.title("Cifrado y Descifrado")
root.geometry("650x565")

def cerrar_sesion():
    root.destroy()
    subprocess.Popen(['python', 'login.py'])

def generar_contrasena_btn():
    try:
        algoritmo_seleccionado = algorithm_var.get()
        generar_contrasena(algoritmo_seleccionado, nombre_usuario)
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar la contraseña: {str(e)}")

def verificar_seguridad_btn():
    password = password_entry.get()
    resultado = verificar_seguridad(password)
    seguridad_label.config(text=resultado)

# Algoritmos disponibles
algorithms = ['MD5', 'SHA-256', 'AES-256', 'Blowfish', 'Triple DES']
algorithm_var = tk.StringVar(value='AES-256')

# Contenedor principal
main_frame = tk.Frame(root, bg="#1E1E2E")
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Primera columna
column1 = tk.Frame(main_frame, bg="#1E1E2E")
column1.pack(side="left", padx=10, fill="y")

# Segunda columna
column2 = tk.Frame(main_frame, bg="#1E1E2E")
column2.pack(side="right", padx=10, fill="y")

# --- Elementos de la Primera Columna ---
tk.Label(
    column1, bg="#1E1E2E", fg="#FFD700", font=("Helvetica", 16, "bold"), 
    text=f"Bienvenido: {nombre_usuario}"
).pack(pady=(20, 5))

tk.Label(
    column1, bg="#1E1E2E", fg="#C6FF62", font=styles.font_style, 
    text="Texto a cifrar/descifrar:"
).pack(pady=(10, 5))

text_entry = tk.Entry(
    column1, width=40, font=styles.font_style(), bd=2, relief="solid"
)
text_entry.pack(pady=5)

tk.Label(
    column1, bg="#1E1E2E", fg="#C6FF62", font=styles.font_style, 
    text="Clave (opcional):"
).pack(pady=(10, 5))

key_entry = tk.Entry(
    column1, width=40, font=styles.font_style(), bd=2, relief="solid"
)
key_entry.pack(pady=5)

tk.Label(
    column1, bg="#1E1E2E", fg="#C6FF62", font=styles.font_style, 
    text="Seleccione el algoritmo:"
).pack(pady=(10, 5))

for algo in algorithms:
    tk.Radiobutton(
        column1, text=algo, variable=algorithm_var, value=algo,
        bg="#1E1E2E", fg="white", font=styles.font_style(), 
        selectcolor="#C6FF62", activebackground="#1E1E2E", activeforeground="white"
    ).pack(anchor="w", padx=20)

encrypt_btn = tk.Button(column1, text="Cifrar", 
                        command=lambda: main_tkinter.encrypt_text(text_entry, key_entry, algorithm_var), width=15)
decrypt_btn = tk.Button(column1, text="Descifrar", 
                        command=lambda: main_tkinter.decrypt_text(text_entry, key_entry, algorithm_var), width=15)
styles.style_button(encrypt_btn)
styles.style_button(decrypt_btn)
encrypt_btn.pack(pady=(15, 5))
decrypt_btn.pack(pady=5)

# --- Elementos de la Segunda Columna ---
tk.Label(
    column2, bg="#1E1E2E", fg="#C6FF62", font=styles.font_style, 
    text="Seleccione algoritmo:"
).pack(pady=(10, 5))

for algo in algorithms:
    tk.Radiobutton(
        column2, text=algo, variable=algorithm_var, value=algo,
        bg="#1E1E2E", fg="white", font=styles.font_style(), 
        selectcolor="#C6FF62", activebackground="#1E1E2E", activeforeground="white"
    ).pack(anchor="w", padx=20)

generar_pass_btn = tk.Button(column2, text="Generar contraseña", command=generar_contrasena_btn, width=20)
styles.style_button(generar_pass_btn)
generar_pass_btn.pack(pady=(15, 5))

password_label = tk.Label(
    column2, text="Ingrese una contraseña:", bg="#1E1E2E", fg="#C6FF62", font=styles.font_style
)
password_label.pack(pady=(20, 5))

password_entry = tk.Entry(
    column2, width=30, font=styles.font_style(), bd=2, relief="solid"
)
password_entry.pack(pady=5)

seguridad_label = tk.Label(
    column2, bg="#1E1E2E", fg="#C6FF62", font=styles.font_style, 
    text=""
)
seguridad_label.pack(pady=5)

verificar_btn = tk.Button(column2, text="Verificar seguridad", command=verificar_seguridad_btn, width=20)
styles.style_button(verificar_btn)
verificar_btn.pack(pady=10)

close_btn = tk.Button(column2, text="Cerra sesion", command=cerrar_sesion, width=15)
styles.style_button_close(close_btn)
close_btn.pack(pady=(30, 5))

# Ejecutar la ventana principal
root.mainloop()