# 1. Crear una variable "cadena" que cotiene el texto "Esto es un texto de ejemplo"
cadena = "Esto es un texto de ejemplo"
print(cadena)

# 2. Crear una variable "longitud" que contiene la longitud de la variable "cadena"
longitud = len(cadena)
print(longitud)

# 3. Crear una variable "strLongitud" que tenga el valor de la "longitud" pero convertido a cadena
#    de caracteres o string
strLongitud = str(longitud)
print("la cadena de caracteres tiene una longitud de "+strLongitud)

# 4. Crear una variable "mayusculas" que contiene la variable "cadena" en mayusculas
mayusculas = cadena.upper()
print(mayusculas)

# 5. Crear una variable "resultado" que concatena "mayusculas" con el texto "tiene longitud de" 
#    y "strLongitud"
resultado = mayusculas + " tiene longitud de " + strLongitud
print(resultado)
