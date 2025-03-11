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
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print("Este coche es de la marca {} de color {} de {} y una cilindrada de {}"
            .format(self.marca, self.color, self.combustible, self.cilindrada))

#llamada a la clase

coche1 = Coche("Citroen","rojo","gasolina","1.6")
print(coche1.color)

coche1.mostrar_caracteristicas()


