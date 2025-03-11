#Doctest

def sumar(numero1, numero2):
    """
    Esto es la documentacion de esta funcion.
    Recibe dos numeros como parametros y devuelve su suma

    >>> sumar(4,3)
    7

    >>> sumar(5,4)
    9

    >>> sumar(1,3)
    7
    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)



import doctest
doctest.testmod()

#  python -u "c:\Users\mento\Desktop\curso_python\seccion_17\116_doctest.py" -v