import sqlite3

conexion = sqlite3.connect("mi_base_de _datos_1.bd")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
personas =cursor.fetchall()

for persona in personas:
    print(persona)