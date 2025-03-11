#diccionarios

diccionarios_colores = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}
print(diccionarios_colores)

print(diccionarios_colores["red"])

valor = diccionarios_colores["yellow"]
print(valor)

diccionarios_colores["black"] = "negro"
print(diccionarios_colores)

diccionarios_colores["yellow"]
print(diccionarios_colores)

del(diccionarios_colores["black"])
print(diccionarios_colores)

for color in diccionarios_colores:
    print(color)

for clave,valor in diccionarios_colores.items():
    print(clave, valor)




