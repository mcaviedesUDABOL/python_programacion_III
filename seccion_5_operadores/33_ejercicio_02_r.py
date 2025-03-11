# 1. Crear una variable "minimo" que tenga el valor 20
minimo = 20
# 2. Crear una variable "maximo" que tenga el valor 500
maximo = 500
# 3. Recoger n valor por teclado y almacenarlo en la variable "dato"
print("ingrese un valor cualquiera por teclado")
dato = input()
# 4. Convertir la varable "dato" en un numero y almacenarlo en la variable "numero"
numero = int(dato)
# 5. si el "numero" es menor que el valor de "minimo" mostrar el texto "valor bajo"
if(numero < minimo):
    print("valor bajo")
# 6. si el "numero" es mayor que el valor de "maximo" mostrar el texto "valor alto"
if(numero >maximo):
    print("valor alto")
# 7. si el "numero" esta entre el valor de "minimo" y "maximo" mostrar el texto "valor medio"
if(numero >minimo) and (numero < maximo):
    print("valor medio ")