# Clases y objetos. POO
class ClaseSilla:
    color = "blanco"
    precio = 100

objetoSilla = ClaseSilla()

print(objetoSilla.color)

print(objetoSilla.precio)

objetoSilla2 = ClaseSilla()
objetoSilla2.color = "verde"
objetoSilla2.precio = 120

print(objetoSilla2.color)

print(objetoSilla2.precio)

# la clase persona

class Persona:
    #metodo constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, no llamo {} y tengo {} anios".format(self.nombre, self.edad))

persona1 = Persona("Juan",37)

print(persona1.nombre)

print(persona1.edad)

print (persona1.saludar())

