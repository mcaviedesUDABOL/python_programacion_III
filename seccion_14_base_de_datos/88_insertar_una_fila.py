#   SQLite - insertar un dato en una tabla

import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Miguel','Caviedes','Malfert',41)")

conexion.commit()

conexion.close()