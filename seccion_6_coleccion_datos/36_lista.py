#listas
colores = ["rojo", "amarillo", "verde"]
print(colores)
print(colores[0])
print(colores[1])
colores[1] = "azul"
print(colores)
print(len(colores))
colores.append("naranja")
print(colores)
colores.remove("rojo")
print(colores)
for Color in colores:
    print(Color)
colores.clear()
print(colores)
