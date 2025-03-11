"""
    Crear el diccionario "frutas"
    frutas ={ "manzana":"apple", "naranja":"orange", "platano":"banana", "limon:"lemon"}

Grabar esta estructura de datos "frutas" en un fichero binario "fichero.pckl"
Ya que en un fichero de texto, solo se guardan caracteres, pero no se pueden guardar ests estucturas

Recuperar esta estructura de datos del fichero "fichero.pckl"
Verificar que sigue siendo un diccionario, ejecutando el metodo .values()
"""

frutas ={ "manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}

print(frutas.values())

fichero = open("seccion_11_ficheros_binarios//fichero1.pckl","wb")

#abrir el fichero binario
import pickle

pickle.dump(frutas,fichero)
fichero.close()

#abrir el fichero binario 2

fichero2 = open("seccion_11_ficheros_binarios//fichero1.pckl","rb")
datos = pickle.load(fichero2)
print(datos)
print(frutas.values())

