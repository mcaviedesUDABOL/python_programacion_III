#funciones lambda

resultado = lambda numero : numero + 30
print(resultado(10))

#funcion normal
print("funcion normal")
def resultado_normal(numero):
    numero += 30 # numero = numero = 30
    return numero
devuelto = resultado_normal(10)
print(devuelto)


print("otras funciones lambda")
resultado_2 = lambda numero_1, numero_2: numero_1 + numero_2
print(resultado_2(5,8))

"""
Crear una funcion Lambda que calcule la media de 3 notas
"""

media = lambda nota_1, nota_2, nota_3: (nota_1 + nota_2 + nota_3)/3
print(media(4,5,6))

