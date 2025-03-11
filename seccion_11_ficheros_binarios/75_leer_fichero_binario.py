import pickle

fichero = open("seccion_11//fichero_colores.pckl","rb")

lista_leida_fichero = pickle.load(fichero)

print(lista_leida_fichero)
