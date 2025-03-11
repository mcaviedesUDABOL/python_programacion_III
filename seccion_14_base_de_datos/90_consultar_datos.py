#   SQLite - consultar datos

import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()
