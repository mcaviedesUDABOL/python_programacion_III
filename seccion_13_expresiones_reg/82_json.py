#JSON
# Convertir datos de un diccionario Python a una estructura JSON
producto1 = {"nombre":"silla", "color":"blanco", "precio":80}
import json
estructura_json = json.dumps(producto1)
print(estructura_json)

"""
print(estructura_json["nombre"])

"""

print(estructura_json[0])

#convertir una estructura JSON (esturtura_json) en un diccionario en Python

producto2 = json.loads(estructura_json)
print(producto2)
