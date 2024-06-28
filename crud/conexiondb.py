import psycopg2
from psycopg2 import connect, OperationalError 

def get_db_connection():
    try:
        conn = connect(
            dbname="crud_finanzas",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        print("Conexión establecida correctamente")
        return conn
    except OperationalError as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None