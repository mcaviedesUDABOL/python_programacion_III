"""
    Crearemos una variable "nota" que tenga el valor de 4.5
    Crearremos una variable "trabajo_realizado" que tenga el valor de "si"
    Calcular el valor de la variable "nota_final", teniendo en cuenta que, si la nota_final es mayor o igual a 4,
    y el valor de la variable "trabajo_variable" es igual a "si", entonces "nota_final" sera igual a "aprobado",
    en caso contrario sera "suspendido"

"""
nota = 4.5
tranbajo_realizado = 'si'
if(nota>=4) and (tranbajo_realizado=='si'):
    nota_final = 'aprobado'
else:
    nota_final = 'suspenso'
print(nota_final)
