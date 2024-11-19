import tkinter as tk
from tkinter import messagebox
from conexion.conexion import obtener_conexion
from styles import styles
import subprocess
from conexion import consultas
# validar el login
def registro_usuario():
    ventana.destroy()
    subprocess.Popen(['python', 'registro.py'])

def validar_login():
    usuario = entry_usuario.get()
    password = entry_password.get()
    
    try:
        # Obtener la conexión
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # Consulta a SQL
        consulta = consultas.consulta4
        cursor.execute(consulta, (usuario, password))
        
        # Verificar si existe el registro
        resultado = cursor.fetchone()
        if resultado:
            nombre_usuario = resultado[0]
            # Guardar el nombre del usuario en un archivo temporal
            with open("usuario_actual.txt", "w") as file:
                file.write(nombre_usuario)
            messagebox.showinfo("Inicio de sesión", f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
            ventana.destroy()  # cerrar el login
            subprocess.Popen(['python', 'main.py'])  # Abre main.py
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("400x275")
ventana.configure(bg="#2E2E2E")

label_usuario = tk.Label(ventana, text="Usuario:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana, width=30, font=styles.font_style)
entry_usuario.pack(pady=5)

label_password = tk.Label(ventana, text="Contraseña:", bg="#2E2E2E", fg="#C6FF62", font=styles.font_style)
label_password.pack(pady=5)
entry_password = tk.Entry(ventana, show="*", width=30, font=styles.font_style)
entry_password.pack(pady=5)

# Botón de inicio de sesión
boton_login = tk.Button(ventana, text="Iniciar sesión", command=validar_login)
styles.style_button(boton_login)  # Aplicar estilo al botón
boton_login.pack(pady=10)

boton_crear_usuario = tk.Button(ventana, text="Crear Usuario", command=registro_usuario)
styles.style_button(boton_crear_usuario)  # Aplicar estilo al botón
boton_crear_usuario.pack(pady=10)

# Ejecutar la interfaz gráfica
ventana.mainloop()
