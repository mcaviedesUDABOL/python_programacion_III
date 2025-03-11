
import sqlite3

conexion = sqlite3.connect("mi_base_de _datos_1.bd")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('Miguel','Caviedes','Malfert',43)")
conexion.commit()
conexion.close()