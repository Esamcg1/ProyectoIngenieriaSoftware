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
    # Listado de contraseñas comunes y secuencias típicas
    comunes = ["password", "123456", "qwerty", "abc123", "111111", "123123", "letmein", "iloveyou", "admin", "root", "sa", ""]
    secuencias = r'(1234|abcd|qwerty|asdf|zxcv|password|5678|8765|0987|4321|123456789|987654321|9876543210|1234567890)'
    
    # Verificar longitud mínima
    if len(password) < 12:
        resultado = "Débil: La contraseña debe tener al menos 12 caracteres."
    # Verificar al menos una letra mayúscula
    elif not re.search(r'[A-Z]', password):
        resultado = "Débil: La contraseña debe incluir al menos una letra mayúscula."
    # Verificar al menos una letra minúscula
    elif not re.search(r'[a-z]', password):
        resultado = "Débil: La contraseña debe incluir al menos una letra minúscula."
    # Verificar al menos un número
    elif not re.search(r'\d', password):
        resultado = "Débil: La contraseña debe incluir al menos un número."
    # Verificar al menos un carácter especial
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        resultado = "Débil: La contraseña debe incluir al menos un carácter especial."
    # Verificar si es una contraseña común
    elif password.lower() in comunes or re.search(secuencias, password.lower()):
        resultado = "Débil: La contraseña es demasiado común o predecible."
    # Verificar caracteres repetidos consecutivos (máximo 3 iguales consecutivos)
    elif re.search(r'(.)\1{3,}', password):
        resultado = "Débil: La contraseña contiene demasiados caracteres repetidos consecutivos."
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


def obtener_contrasenas_usuario(id_usuario):
    """
    Recupera las contraseñas generadas por el usuario actual de la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Consulta para obtener las contraseñas del usuario
        id_usuario = obtener_id_usuario(nombre_usuario, cursor)
        query = "SELECT pass_sugerida FROM pass_sugerida WHERE id_usuario = ?"
        cursor.execute(query, (id_usuario,))
        resultados = cursor.fetchall()

        # Extraer solo las contraseñas como una lista
        return [fila[0] for fila in resultados]
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener contraseñas: {str(e)}")
        return []
    finally:
        if conexion:
            conexion.close()


def validar_login(usuario, password):
    try:
        # Obtener la conexión
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # Consulta para validar usuario
        consulta = consultas.consulta4
        cursor.execute(consulta, (usuario, password))
        
        # Verificar si existe el registro
        resultado = cursor.fetchone()
        if resultado:
            nombre_usuario = resultado[0]
            
            # Obtener el ID del usuario
            consulta_id_usuario = "SELECT id_usuario FROM usuario WHERE usuario = ?"
            cursor.execute(consulta_id_usuario, (usuario,))
            id_usuario = cursor.fetchone()[0]
            
            # Insertar el registro de inicio de sesión
            consulta_insert_login = consultas.consulta6
            cursor.execute(consulta_insert_login, (id_usuario,))
            conn.commit()
            
            # Retornar éxito y datos del usuario
            return True, nombre_usuario
        else:
            # Retornar fallo de autenticación
            return False, "Usuario o contraseña incorrectos."

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        
    except Exception as e:
        # Manejar errores de conexión
        return False, f"Error de conexión: {e}"