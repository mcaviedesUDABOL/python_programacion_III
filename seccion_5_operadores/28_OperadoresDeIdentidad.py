# Operadores de identidad (is, is not)

frutas1 = ["manzana", "pera"]
frutas2 = ["manzana", "pera"]
frutas3 = frutas1

print(frutas1)
print(frutas2)
print(frutas3)
# is
print(frutas3 is frutas1)
frutas3.append("naranja")
print(frutas3)
print(frutas1)

#is not

print(frutas3 is not frutas1)