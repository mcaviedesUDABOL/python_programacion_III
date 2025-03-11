import sqlite3

conexion = sqlite3.connect("mi_base_de _datos_1.bd")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")
conexion.commit()
conexion.close()