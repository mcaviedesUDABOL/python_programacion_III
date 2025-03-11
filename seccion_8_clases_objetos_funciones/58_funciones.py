# Funciones

def saludar():
    print("Buenos dias")

print(saludar())


def saludo(nombre):
    print("Buenos dias "+nombre)

nombre= "Juan"

print(saludo(nombre))

def sumar(numero1, numero2):
    suma = numero1 + numero2
    return suma


numero1 = 5
numero2 = 3

resultado = sumar(numero1, numero2)

print(resultado)

# paso por valor por referencia

colores = ["rojo", "verde", "azul"]

def incluir_color(colores,color):
    colores.append(color)

color = "negro"
incluir_color(colores, color)

print(colores)

