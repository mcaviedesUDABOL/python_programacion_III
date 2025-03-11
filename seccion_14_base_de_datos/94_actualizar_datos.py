#   SQLite - actualizar los datos de una columna
import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET edad=30 WHERE nombre='Mario'")

conexion.commit()

conexion.close()