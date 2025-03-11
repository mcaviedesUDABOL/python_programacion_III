import pickle

lista_colores = ["azul", "verder", "rojo", "amarillo"]

fichero = open("seccion_11_ficheros_binarios//fichero_colores.pckl","wb")

pickle.dump(lista_colores, fichero)

fichero.close()
