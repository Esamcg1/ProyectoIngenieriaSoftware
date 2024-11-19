import tkinter as tk
from tkinter import messagebox
from conexion.conexion import obtener_conexion
from styles import styles
import subprocess 
from conexion import consultas

def registrar_usuario():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    usuario = entry_usuario.get()
    password = entry_password.get()

    if not (nombre and apellido and usuario and password):
        messagebox.showwarning("Campos incompletos", "Por favor, completa los campos obligatorios.")
        return

    try: 
        conn = obtener_conexion()
        cursor = conn.cursor()

        consulta = consultas.consulta5
        cursor.execute(consulta, (nombre, apellido, edad, correo, usuario, password))
        conn.commit()

        messagebox.showinfo("Crear usuario", "Usuario creado con éxito")
        ventana.destroy()  # cerrar registro
        subprocess.Popen(['python', 'login.py'])  # Abre login.py
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Registrarse")
ventana.geometry("500x600")
ventana.configure(bg="#2E2E2E")

label_nombre = tk.Label(ventana, text="Nombre:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30, font=styles.font_style)
entry_nombre.pack(pady=5)

label_apellido = tk.Label(ventana, text="Apellido:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_apellido.pack(pady=5)
entry_apellido = tk.Entry(ventana, width=30, font=styles.font_style)
entry_apellido.pack(pady=5)

label_edad = tk.Label(ventana, text="Edad:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_edad.pack(pady=5)
entry_edad = tk.Entry(ventana, width=30, font=styles.font_style)
entry_edad.pack(pady=5)

label_correo = tk.Label(ventana, text="Correo:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_correo.pack(pady=5)
entry_correo = tk.Entry(ventana, width=30, font=styles.font_style)
entry_correo.pack(pady=5)

label_usuario = tk.Label(ventana, text="Usuario:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana, width=30, font=styles.font_style)
entry_usuario.pack(pady=5)

label_password = tk.Label(ventana, text="Contraseña:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_password.pack(pady=5)
entry_password = tk.Entry(ventana, show="*", width=30, font=styles.font_style)
entry_password.pack(pady=5)

# Botón de creación de usuario
boton_creacion_usuario = tk.Button(ventana, text="Crear mi usuario", command=registrar_usuario)
styles.style_button(boton_creacion_usuario)
boton_creacion_usuario.pack(pady=10)

ventana.mainloop()