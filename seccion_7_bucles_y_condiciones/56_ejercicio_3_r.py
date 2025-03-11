""""
    1. Crear una variable "inicio" con el valor de 1
    2. Crear una variable "fin" con el valor de 6
    3. Hacer un bucle While que muestre tantas filas como valores haya entre "inicio" y "fin"
    4. En cada iteracion del bucle mostrar el texto "Esta es la fila" + numero de fila en la que esta
"""

inicio =1
fin = 6
while(inicio <fin):
    texto = "Esta es la fila " + str(inicio)
    print(texto)
    inicio = inicio + 1
