import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos
def conectar():
    try:
        # Aquí se establecen los datos para conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            database="TiendaOnline",
            user="root",
            password="curso"  # Contraseña para la base de datos
        )
        return conexion  # Si conecta, devuelve la conexión
    except Error as e:
        # Si algo falla, muestro el error
        print(f"Error al conectar con la base de datos: {e}")
        return None  # Si hay fallo, devuelve None
