#   SQLite - consultar datos que cumplan una determinada codicion
import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad > 50")

personas = cursor.fetchall()

for persona in personas:
    print(persona)

conexion.close()