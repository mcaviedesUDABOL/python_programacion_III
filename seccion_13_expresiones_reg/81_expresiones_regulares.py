# Expresiones regulares (search, findall, split, sub)

texto = "Hola, mi nombre es Miguel"

import re

print(re.search("nombre", texto))

print(re.search("adios", texto)) # no devuelve nada si no lo encuentra

resultado = re.search("nombre",texto)
if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena NO encontrada")

print(re.search("Miguel$", texto)) #busca al final de la cadena
print(re.search("^Hola",texto)) # busca al rpincipio de la cadena
print(re.search("mi.*es",texto)) #buscar en el medio  


#findall
texto = """
El coche de Miguel es rojo,
el coche de Antonio es blanco,
y el coche de Maria es rojo
"""
print(re.findall("coche.*rojo",texto))

# sub
texto = "La silla es blanca y vale 80"
print(texto)
re.sub("blanca","roja",texto) #?
print(texto)


#split

texto = "La silla es blanca y vale 80"
print(re.split("\s",texto))



