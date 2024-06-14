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
