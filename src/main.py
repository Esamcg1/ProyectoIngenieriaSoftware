import tkinter as tk
from styles import styles
from tkinter import messagebox
from conexion.conexion import obtener_conexion
import main_tkinter
import logica
import pyperclip
import re
from conexion import consultas
from funciones.funciones import verificar_seguridad, generar_contrasena
# Leer el nombre del usuario del archivo temporal
try:
    with open("usuario_actual.txt", "r") as file:
        nombre_usuario = file.read()
except FileNotFoundError:
    nombre_usuario = "Usuario"

# Crear la ventana principal
root = tk.Tk()
root.configure(bg="#2E2E2E")
root.title("Cifrado y Descifrado")
root.geometry("490x555")
    
def generar_contrasena_btn():
    try:
        algoritmo_seleccionado = algorithm_var.get()  # Obtener algoritmo actual seleccionado
        generar_contrasena(algoritmo_seleccionado, nombre_usuario)  # Llamar a la función con los argumentos necesarios
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar la contraseña: {str(e)}")

def verificar_seguridad_btn():
    password = password_entry.get()  # Obtener la contraseña ingresada
    resultado = verificar_seguridad(password)  # Verificar la seguridad de la contraseña
    seguridad_label.config(text=resultado)
    

algorithms = ['MD5', 'SHA-256', 'AES-256', 'Blowfish', 'Triple DES']
algorithm_var = tk.StringVar(value='AES-256')
root.geometry("650x565")
# Crear contenedor principal con dos columnas
main_frame = tk.Frame(root, bg="#2E2E2E")
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Primera columna (Cifrar/Descifrar)
column1 = tk.Frame(main_frame, bg="#2E2E2E")
column1.pack(side="left", padx=10, fill="y")

# Segunda columna (Generar contraseña)
column2 = tk.Frame(main_frame, bg="#2E2E2E")
column2.pack(side="right", padx=10, fill="y")

# --- Elementos para la Primera Columna ---
tk.Label(column1, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text=f"Bienvenido: {nombre_usuario}").pack(pady=(20, 5))
tk.Label(column1, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Texto a cifrar/descifrar:").pack(pady=(10, 5))
text_entry = tk.Entry(column1, width=40, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
text_entry.pack(pady=5)

tk.Label(column1, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Clave (opcional):").pack(pady=(10, 5))
key_entry = tk.Entry(column1, width=40, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
key_entry.pack(pady=5)

tk.Label(column1, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Seleccione el algoritmo:").pack(pady=(10, 5))
for algo in algorithms:
    tk.Radiobutton(
        column1, text=algo, variable=algorithm_var, value=algo,
        bg="#2E2E2E", fg="white", font=("Arial", 10), selectcolor="#C6FF62",
        activebackground="#2E2E2E", activeforeground="white"
    ).pack(anchor="w", padx=20)

encrypt_btn = tk.Button(column1, text="Cifrar", 
                        command=lambda: main_tkinter.encrypt_text(text_entry, key_entry, algorithm_var), width=15)
decrypt_btn = tk.Button(column1, text="Descifrar", 
                        command=lambda: main_tkinter.decrypt_text(text_entry, key_entry, algorithm_var), width=15)
styles.style_button(encrypt_btn)
styles.style_button(decrypt_btn)
encrypt_btn.pack(pady=(15, 5))
decrypt_btn.pack(pady=5)

# --- Elementos para la Segunda Columna ---
tk.Label(column2, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style, text="Seleccione algoritmo:").pack(pady=(10, 5))
for algo in algorithms:
    tk.Radiobutton(
        column2, text=algo, variable=algorithm_var, value=algo,
        bg="#2E2E2E", fg="white", font=("Arial", 10), selectcolor="#C6FF62",
        activebackground="#2E2E2E", activeforeground="white"
    ).pack(anchor="w", padx=20)

generar_pass_btn = tk.Button(column2, text="Generar contraseña", command=generar_contrasena_btn, width=20)
styles.style_button(generar_pass_btn)
generar_pass_btn.pack(pady=(15, 5), anchor="center")

password_label = tk.Label(column2, text="Ingrese una contraseña:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
password_label.pack(pady=(20, 5), anchor="center", fill="x")

password_entry = tk.Entry(column2, width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
password_entry.pack(pady=5, anchor="center", fill="x")

# Crear un label para mostrar el resultado de la verificación de seguridad
seguridad_label = tk.Label(column2, bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
seguridad_label.pack(pady=5, anchor="center", fill="x")

# Botón para verificar seguridad
verificar_btn = tk.Button(column2, text="Verificar seguridad", command=verificar_seguridad_btn, width=20)
styles.style_button(verificar_btn)
verificar_btn.pack(pady=10, anchor="center")

close_btn = tk.Button(column2, text="Salir", command=root.destroy, width=15)
styles.style_button_close(close_btn)
close_btn.pack(pady=(30, 5))

# Ejecutar la ventana principal
root.mainloop()

