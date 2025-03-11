"""
Crear un diccionario con los siguientes pares de valores
    manzana = apple
    naranja = orange
    platano = banana
    limon = lemon
Muestra la traduccion para la palabra "naranja"
Aniade un elemento nuevo con "pinia" y "pineapple"
Hay un bucle para mostrar todos los elementos del diccionario

"""

frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
print(frutas)

print(frutas["naranja"])

frutas["pinia"] = "pineapple"
print(frutas)

for clave, valor in frutas.items():
    print("{} en ingles es {}".format(clave,valor))

