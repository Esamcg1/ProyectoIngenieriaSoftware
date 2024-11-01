import pyodbc

SERVER = 'DESKTOP-I12P5CF'
DATABASE = 'proyectofaseII'
USERNAME = ''  
PASSWORD = ''  

def obtener_conexion():
    connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
    conn = pyodbc.connect(connectionString)
    return conn

    # except pyodbc.Error as e:
    #     print("Error en la conexion :(", e)
