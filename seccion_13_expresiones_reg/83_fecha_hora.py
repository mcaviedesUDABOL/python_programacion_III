#fecha y hora
from datetime import datetime

fechaHora =  datetime.now()

print(fechaHora)

anio = fechaHora.year
print(anio)
mes = fechaHora.month
print(mes)
dia = fechaHora.day
print(dia)
#hora

hora = fechaHora.hour
minutos =fechaHora.minute
segundos = fechaHora.second
micorsegundos = fechaHora.microsecond

print("La hora es {}:{}:{}".format(hora,minutos,segundos))


