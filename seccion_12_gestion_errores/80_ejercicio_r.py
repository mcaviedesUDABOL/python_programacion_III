"""
Ejercicio
Crear la funcion "operacion" que dado 3 numeros, divida el primer numero entre 
la resta de los otros dos numeros
Utilizar la funcion creada con los numeros 5,4,2
Utilizar la funcion creada con los numeros 6,3,3
Utilizar el bloque ... expect para controlar cualquier posible error
"""

def operacion(numero1, numero2, numero3):
    resultado = numero1 / (numero2 - numero3)
    return resultado

numero1 = 5#6
numero2 = 4#3
numero3 = 3#3
resultado = operacion(numero1, numero2, numero3)
print(resultado)

#colocar el try
numero1 = 6
numero2 = 3
numero3 = 3
try:
    resultado = operacion(numero1, numero2, numero3)
    print(resultado)
except:
    print("Error. Los ultimos dos numeros tienen que ser diferentes")