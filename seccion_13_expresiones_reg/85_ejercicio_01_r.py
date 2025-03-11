"""
    Crear una funcion "buscar" que mediante la expresion regular indique que una palabra esta en una frase
    Probar la funcion "buscar" con estas fraces
    texto="Esto es una frease de pruebas para hacer busquedas
    En caso  de encontrar la palabra en la frase, indica en que posicion empieza y en vial finaliza
"""
import re

def buscar(palabra, texto):
    resultado = re.search(palabra,texto)
    return resultado

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra = "frases"
#palabra = "una"

resultado = buscar(palabra,texto)

if(resultado):
    print("Palabra {} encontrada".format(palabra))
    inicial  = resultado.start()
    final = resultado.end()
    print("Empieza en la posicion {} y finalizacion en la posicion {}".format(inicial, final))
else:
    print("Palabra {} no encontarada".format(palabra))



