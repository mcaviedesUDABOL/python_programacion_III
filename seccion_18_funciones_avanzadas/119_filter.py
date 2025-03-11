#filter funcion para filtrar resultados segun una condicion

def positivo(numero):
    if(numero >0 ):
        return True
    else:
        return False


positivo(5)

positivo(-3)

numeros = [4,-2,8,-3,-5,-7,1,9]

filtro = filter(positivo, numeros)

resultado = list(filtro)

print(resultado)
