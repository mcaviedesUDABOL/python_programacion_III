
import sqlite3

conexion = sqlite3.connect("mi_base_de _datos_1.bd")
cursor = conexion.cursor()
lista_personas = [('Pedro','Rodriguez','Perez',56), ('Mario','Lopez','Borda',45),('Luis','Gonzalez','Perez',46)]
cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?,?)",lista_personas)
conexion.commit()
conexion.close()


