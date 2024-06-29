import psycopg2
from psycopg2 import connect, OperationalError 

def get_db_connection():
    try:
        conn = connect(
            dbname="crud_finanzas",
            user="postgres",
            password="Angi#Mono",
            host="localhost",
            port="5432"
        )
        print("Conexión establecida correctamente")
        return conn
    except OperationalError as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None
        
# Ejecución de la función para probar la conexión
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        connection.close()
