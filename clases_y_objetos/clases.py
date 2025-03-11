#clases y objetos POO

class ClaseSilla:
    #atributos
    color = "blanco"
    precio = 100

objetoSilla = ClaseSilla()
print(type(objetoSilla))
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
        print("Hola, me llamo {} y tengo {} años".format(self.nombre, self.edad))


mi_persona = Persona("Miguel", 43)
print(mi_persona.nombre)
print(mi_persona.edad)
mi_persona.saludar()

"""
crear una clase "Coche" que tenga los siguientes atributos:
    marca, color, combustible, cilindrada
Crear la funcion "__init__" que se asigna los parametros de la clase a los atributos de la clase
Crear otra funcion "mostrar_caracteristicas" que mediante print muestre en pantalla las 
caracteristicas (o atributos) que tiene el coche
Crear un objeto "coche1"  con los atriburos "Opel", "rojo", "gasolina", "1.6"
Ejecutar la funcion "mostrar_caracteristicas" del objeto "coche1"
"""

class Coche:

    def __init__(self,marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print("Este coche es de la marca {} de color {}, de {} y de cilindrada {}"
              .format(self.marca, self.color, self.combustible, self.cilindrada))

#llamar a la clase

coche_1 = Coche("Citroen","rojo","gasolina","1.6")
coche_1.mostrar_caracteristicas()
print(coche_1.color)