import tkinter as tk
from tkinter import messagebox
from conexion.conexion import obtener_conexion
from styles import styles
import subprocess
from conexion import consultas
from funciones.funciones import validar_login
from styles import elements
# validar el login
def registro_usuario():
    ventana.destroy()
    subprocess.Popen(['python', 'registro.py'])


def on_login():
    usuario = entry_usuario.get()
    password = entry_password.get()
    # Llamar a la función validar_login desde funciones.py
    exito, mensaje = validar_login(usuario, password)
    if exito:
        # Guardar el nombre del usuario en un archivo temporal
        with open("usuario_actual.txt", "w") as file:
            file.write(mensaje)
        messagebox.showinfo("Inicio de sesión", f"Inicio de sesión exitoso. Bienvenido, {mensaje}.")
        ventana.destroy()  # Cerrar el login
        subprocess.Popen(['python', 'main.py'])  # Abrir main.py
    else:
        messagebox.showerror("Error", mensaje)

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("400x350")
ventana.configure(bg="#1E1E2E")
# Encabezado llamativo
header = tk.Label(
    ventana, text="Bienvenido", font=("Helvetica", 18, "bold"), 
    fg="#FFD700", bg="#1E1E2E", pady=10
)
header.pack()

# Campos de usuario
label_usuario = tk.Label(
    ventana, text="Usuario:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style()
)
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(
    ventana, width=30, font=styles.font_style(), bd=2, relief="solid"
)
entry_usuario.pack(pady=5)

# Campos de contraseña
label_password = tk.Label(
    ventana, text="Contraseña:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style()
)
label_password.pack(pady=5)
entry_password = tk.Entry(
    ventana, show="*", width=30, font=styles.font_style(), bd=2, relief="solid"
)
entry_password.pack(pady=5)

# Botón de inicio de sesión
boton_login = tk.Button(ventana, text="Iniciar sesión", command=on_login)
styles.style_button(boton_login)  # Aplicar estilo al botón
boton_login.pack(pady=15)

# Botón de registro de usuario
boton_crear_usuario = tk.Button(ventana, text="Crear Usuario", command=registro_usuario)
styles.style_button(boton_crear_usuario)  # Aplicar estilo al botón
boton_crear_usuario.pack(pady=5)

# Footer
footer = tk.Label(
    ventana, text="© 2024 Mi app UDV", bg="#1E1E2E", fg="#8A8A8A", 
    font=("Helvetica", 10, "italic")
)
footer.pack(side="bottom", pady=10)

# Ejecutar la interfaz gráfica
ventana.mainloop()
