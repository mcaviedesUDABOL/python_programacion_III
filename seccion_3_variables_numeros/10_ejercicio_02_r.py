# 1. Crear una variable "numero1" que tenga el valor de 5

numero1 = 5
print(numero1)

# 2. Crear otra varivale "numero2" que tenga el valor de 3

numero2 = 3
print(numero2)

# 3. Crear otra variable "suma" que tenga el valor de la suma de los 2 numeros anteriores (numero1, numero2)

suma = numero1 + numero2
print(suma)

# 4. Convertir esta variable "suma" en una cadena de caracteres y llamarla "strSuma"

strSuma = str(suma)
print("resultado de la suma convertido a cadena")
print(strSuma)

# 5. Crear una variable resultado que concatene el texto "El resultado es: " y la variavle "strSuma" (+)

#error
#resultado = "El resultado es: " + suma
resultado = "El resultado es: " + strSuma
print(resultado)