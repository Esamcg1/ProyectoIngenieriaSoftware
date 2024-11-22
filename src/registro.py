import tkinter as tk
from tkinter import messagebox
from conexion.conexion import obtener_conexion
from styles import styles
from conexion import consultas
from funciones.funciones import registrar_usuario

# Función para manejar el registro de usuario
def registrar_usuario_btn():
    # Recoger los valores de los campos de entrada
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    usuario = entry_usuario.get()
    password = entry_password.get()
    registrar_usuario(nombre, apellido, edad, correo, usuario, password, ventana)

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Registrarse")
ventana.geometry("500x600")
ventana.configure(bg="#1E1E2E")

# --- Campo: Nombre ---
label_nombre = tk.Label(ventana, text="Nombre:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style())
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
entry_nombre.pack(pady=5)

# --- Campo: Apellido ---
label_apellido = tk.Label(ventana, text="Apellido:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style())
label_apellido.pack(pady=5)
entry_apellido = tk.Entry(ventana, width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
entry_apellido.pack(pady=5)

# --- Campo: Edad ---
label_edad = tk.Label(ventana, text="Edad:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style())
label_edad.pack(pady=5)
entry_edad = tk.Entry(ventana, width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
entry_edad.pack(pady=5)

# --- Campo: Correo ---
label_correo = tk.Label(ventana, text="Correo:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style())
label_correo.pack(pady=5)
entry_correo = tk.Entry(ventana, width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
entry_correo.pack(pady=5)

# --- Campo: Usuario ---
label_usuario = tk.Label(ventana, text="Usuario:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style())
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana, width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
entry_usuario.pack(pady=5)

# --- Campo: Contraseña ---
label_password = tk.Label(ventana, text="Contrasena:", bg="#1E1E2E", fg="#FFFFFF", font=styles.font_style())
label_password.pack(pady=5)
entry_password = tk.Entry(ventana, show="*", width=30, font=("Arial", 10), relief="flat", highlightbackground="#C6FF62", highlightthickness=1)
entry_password.pack(pady=5)

# --- Botón de creación de usuario ---
boton_creacion_usuario = tk.Button(ventana, text="Crear mi usuario", command=registrar_usuario_btn, width=20)
styles.style_button(boton_creacion_usuario)
boton_creacion_usuario.pack(pady=15)

# --- Botón de cierre ---
boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy, width=15)
styles.style_button_close(boton_cerrar)
boton_cerrar.pack(pady=(20, 5))


footer = tk.Label(
    ventana, text="© 2024 Mi app UDV", bg="#1E1E2E", fg="#8A8A8A", 
    font=("Helvetica", 10, "italic")
)
footer.pack(side="bottom", pady=10)


# Ejecutar la ventana
ventana.mainloop()