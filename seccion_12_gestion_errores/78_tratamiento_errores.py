# try .. expect.. else.. finally
"""
numero1 = 5
numero2 = 0
division = numero1 / numero2 
"""

#try
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except:
    print("Ha habido un error")

"expect"
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")

#else
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")
else:
    print("La division funciono correctamente")


#finally
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print("Error, division entre cero")
except:
    print("Ha habido un error")
else:
    print("La division funciono correctamente")
finally:
    print("Esta prueba del try se ha acabado")