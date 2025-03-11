#imprimir variables de una cadena

nombre = "Miguel"
print("Buenas noches " + nombre)

#.format

nombre = "Miguel"
edad = 18
print("Buenas dias {}, felix {} cumpleanios".format(nombre,edad))

#formate de cadena a numeros antes de impresion en pantalla
resultado = 10 / 3
print(resultado)
print("El resultado es {r}".format(r=resultado))
print("El resultado es {r:1.3f}".format(r=resultado))

# f-strings
nombre = "Antonio"
edad = 30
print(f"Buenos dias {nombre}, feliz {edad} cumpleanios")
