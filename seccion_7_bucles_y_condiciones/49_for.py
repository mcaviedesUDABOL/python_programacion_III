# for 
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)
cadena = "Hola mundo"

for caracter in cadena:
    print(caracter)

range(8)

for numero in range(8):
    print(numero)

for numero in range(3,8):
    print(numero)

for numero in range(3,8,2):
    print(numero)

#break

for numero in range(10):
    if(numero == 5):
        break
    print(numero)


#continue
for numero in range(10):
    if(numero == 6):
        continue
    print(numero)

# doble bucle
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1, numero2)
