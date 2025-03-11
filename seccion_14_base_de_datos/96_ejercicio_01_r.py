"""
Crear una base de datos "basededatos.bd"
Crear una tabla "productos" con 3 campos
    id: Identificador del producto de tipo numerio
    nombre: Nombre del producto de tipo texto
    precio: Precio del producto de tipo numerico
Insertar 3 productos en la tabla "productos"
    1, "Impresoras", 300
    2, "Raton", 20
    3, "Ordenador", 600
Consultar los productos de la tabla "productos"
Cerrar la base de datos "basededatos.db"
"""
import sqlite3

conexion = sqlite3.connect("seccion_14_base_de_datos//basededatos.db")

curso = conexion.cursor()
curso.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER )")

conexion.commit()

curso.execute("INSERT INTO PRODUCTOS VALUES(1,'IMPRESORAS',300)")
conexion.commit()

curso.execute("INSERT INTO PRODUCTOS VALUES(2,'RATON',20)")
conexion.commit()

curso.execute("INSERT INTO PRODUCTOS VALUES(3,'ORDENADOR',600)")
conexion.commit()

curso.execute("SELECT * FROM PRODUCTOS")
productos = curso.fetchall()
for producto in productos:
    print(producto)
conexion.close()

