#   SQLite - insertar varios datos en una tabla

import sqlite3

conexion =sqlite3.connect("seccion_14//basededatos1.db")

cursor = conexion.cursor()

lista_personas = [ ('Pedro','Rodrigues','Perez',56), ('Mario','Lopez','Borda',45),('Luis','Gonzalez','Perez',46)]

cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?,?)",lista_personas)

conexion.commit()

conexion.close()