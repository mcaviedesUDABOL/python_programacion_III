#   SQLite - borrar una tupla
import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre= 'Luis'")

conexion.commit()

conexion.close()