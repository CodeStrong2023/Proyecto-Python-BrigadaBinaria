from Ingresos import Ingresos

class Ingresos: 
    def _init_(self):
        self.conexion = ConectionDB()

    def insert_new_income(self, date, amount, category, description):
        cursor = self.conexion.conectar()
        consulta = "INSERT INTO ingresos (date, amount, category, description) VALUES (%s, %s, %s, %s)"
        valores = (date, amount, category, description)
        cursor.execute(consulta, valores)
        self.conexion.conexion.commit()
        cursor.close()
   
    def obtener_datos_ingreso():
        date = input("Ingrese la fecha del ingreso (YYYY-MM-DD): ")
        amount = float(input("Ingrese el monto del ingreso: "))
        category = input("Ingrese la categoría del ingreso: ")
        description = input("Ingrese la descripción del ingreso: ")
        return date, amount, category, description
