# Map Aplicar una funcion a una lista

def multiplicar(numero):
    return numero * 2

multiplicar(2)

numeros = [2,4,6]

mapeo = map(multiplicar, numeros)

print(mapeo)

resultado = list(mapeo)
print(resultado)


lista_resultados = list(map(multiplicar,numeros))
print(lista_resultados)


lista_resultados = list(map(lambda numero: numero *2, numeros))
print(lista_resultados)

