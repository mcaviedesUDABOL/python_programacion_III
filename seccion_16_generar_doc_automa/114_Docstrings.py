# Docstrings cadenas para documentacion

def saludar(nombre):
    """
        Esto sera un comentario de la funcion saludar.
        Esta funcion recebira como parametro una cadena con el nombre a
        imprimira por pantalla un saludo con el nombre concatenado
    """
    print("Buenos dias "+nombre)

saludar("Miguel")

help(saludar)


class Saludos:
    """
        Esta clase tendra dos funciones buenos_dias y adios
        Ambas funciones recibiran como parametro un nombre
    """
    def buenos_dias(self, nombre):
        """ Esta funcion sirve para decir buenos dias a una persona """
        print("Buenos dias {} ".format(nombre))

    def adios(self, nombre):
        """ Esta funcion dice adios a una persona """
        print("Adios {}".format(nombre))


saludo = Saludos()
saludo.buenos_dias("Miguel")

help(Saludos)