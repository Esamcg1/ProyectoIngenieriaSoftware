import re
import tkinter as tk
from styles import styles
from tkinter import messagebox
from conexion.conexion import obtener_conexion
import pyperclip
import logica
from conexion import consultas
import subprocess

                    #Obtener ID de usuario y algoritmo para diferentes operaciones
def obtener_id_usuario(nombre, cursor):
    query = consultas.consulta1
    cursor.execute(query, (nombre,))
    result = cursor.fetchone()
    return result[0] if result else None

                    # Obtener id_algoritmo (función auxiliar)
def obtener_id_algoritmo(nombre_algoritmo, cursor):
    query = consultas.consulta2
    cursor.execute(query, (nombre_algoritmo,))
    result = cursor.fetchone()
    return result[0] if result else None


                    #Metodo para verificar la seguridad de una contrasena en main.py
def verificar_seguridad(password):
    
    # Criterios para evaluar la seguridad
    if len(password) < 8:
        resultado = "Débil: La contraseña debe tener al menos 8 caracteres."
    elif not re.search(r'[A-Z]', password):
        resultado = "Débil: La contraseña debe incluir al menos una letra mayúscula."
    elif not re.search(r'[a-z]', password):
        resultado = "Débil: La contraseña debe incluir al menos una letra minúscula."
    elif not re.search(r'\d', password):
        resultado = "Débil: La contraseña debe incluir al menos un número."
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        resultado = "Débil: La contraseña debe incluir al menos un carácter especial."
    elif password.lower() in ["password", "123456", "qwerty", "abc123"]:  # Evitar patrones comunes
        resultado = "Débil: La contraseña es demasiado común."
    else:
        resultado = "Fuerte: La contraseña es segura."
    
    # Mostrar el resultado al usuario
    messagebox.showinfo("Seguridad de la Contraseña", resultado)



                    #Metodo para generar una contrasena en main.py
def generar_contrasena(algorithm_var, nombre_usuario):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Generar contraseña
        nueva_password = logica.generate_random_password()
        algoritmo_seleccionado = algorithm_var  # Algoritmo actual seleccionado
        
        # Obtener id_usuario e id_algoritmo
        id_usuario = obtener_id_usuario(nombre_usuario, cursor)
        id_algoritmo = obtener_id_algoritmo(algoritmo_seleccionado, cursor)

        # Validación
        if id_usuario is None:
            raise ValueError("El usuario no existe en la base de datos.")
        if id_algoritmo is None:
            raise ValueError("El algoritmo seleccionado no existe en la base de datos.")

        # Insertar en la base de datos
        query = consultas.consulta3
        cursor.execute(query, (id_usuario, id_algoritmo, nueva_password))
        conexion.commit()

        # Copiar al portapapeles
        pyperclip.copy(nueva_password)

        messagebox.showinfo("Contraseña Generada", f"La contraseña ha sido generada y copiada al portapapeles:\n{nueva_password}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar la contraseña: {str(e)}")
    finally:
        if conexion:
            conexion.close()

                    #Funcion para registra un usuario en registro.py
def registrar_usuario(nombre, apellido, edad, correo, usuario, password, ventana):
    if not (nombre and apellido and usuario and password):
        messagebox.showwarning("Campos incompletos", "Por favor, completa los campos obligatorios.")
        return

    try: 
        conn = obtener_conexion()
        cursor = conn.cursor()

        consulta = consultas.consulta5  # Asegúrate de que esta consulta está definida correctamente
        cursor.execute(consulta, (nombre, apellido, edad, correo, usuario, password))
        conn.commit()

        messagebox.showinfo("Crear usuario", "Usuario creado con éxito")
        ventana.destroy()  # Cierra la ventana de registro
        subprocess.Popen(['python', 'login.py'])  # Abre login.py
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")


