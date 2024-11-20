import main_tkinter
#Obtener id del usuario en main.py    
consulta1 = "SELECT id_usuario FROM usuario WHERE nombre = ?"

#Obtener id del algoritmo usado en main.py:
consulta2 = "SELECT id_algoritmo FROM algoritmos WHERE nombre_algoritmo = ?"

#Insertar la contrasena generada aleatoriamente en main.py
consulta3 = """
        INSERT INTO pass_sugerida (id_usuario, id_algoritmo, pass_sugerida) 
        VALUES (?, ?, ?)
        """

#Validar autenticacion del usuario en login.py
consulta4 = "SELECT nombre FROM usuario WHERE usuario = ? AND pass = ?"

#registras un nuevo usuario en registro.py
consulta5 = "INSERT INTO usuario (nombre, apellido, edad, correo, usuario, pass) VALUES (?, ?, ?, ?, ?, ?);"

#Obtener el ID del algoritmo a partir de la seleccion dada por el usuario en main_tkinter


# Insertar un registro de inicio de sesión en registro_logins
consulta6 = "INSERT INTO registro_logins (id_usuario) VALUES (?)"

#Obtener el ID del usuario para registrar el registro en registro_logins
consulta7 = "SELECT id_usuario FROM usuario WHERE usuario = ?"