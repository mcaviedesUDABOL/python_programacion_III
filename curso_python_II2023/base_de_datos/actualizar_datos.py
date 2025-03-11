import sqlite3

conexion = sqlite3.connect("mi_base_de _datos_1.bd")
cursor = conexion.cursor()
cursor.execute("UPDATE personas SET edad=25 WHERE nombre='Mario'")
conexion.commit()
conexion.close()