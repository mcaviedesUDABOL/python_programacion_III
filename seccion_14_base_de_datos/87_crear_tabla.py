# SQLite3 Crear una tabla en nuestra base de datos

import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

conexion.commit()

conexion.close()