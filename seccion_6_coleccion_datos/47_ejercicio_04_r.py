# 1. Crear una variable "diccionario" con los pares de valores siguientes
#        clave = uno     valor= one
#        clave = dos     valor= two
#        clave = tres     valor= three
diccionario = {"uno":"once", "dos":"two", "tres":"three"}
# 2. Mostrar por pantalla el valor de la varaible "diccionario"
print(diccionario)
# 3. Aniadir un nuevo elemenot al diccionario
#        clave = cuatro    valor= one
diccionario["cuatro"] = "four"
# 4. Mostrar ahora el valor del diccionario
print(diccionario)
# 5. Recoger un valor introcucido por teclado y almacenarlo en "dato"
print("introducir un valor para ver si esta en el diccionario")
dato = input()
# 6. Utilizar "dato" como clave del diccionario para recuperar su valor
valor = diccionario[dato]
print(valor)