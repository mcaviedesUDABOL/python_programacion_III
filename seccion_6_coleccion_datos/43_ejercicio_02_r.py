# 1. Crear una variable "tupla" que sea una tupla de los siguientes nombres: 
# Antonio, Pedro y Maria
tupla = ('Antonio', 'Pedro', 'Maria')
# 2. Mostrar el valor de la variable "tupla"
print(tupla)
# 3. Recoger un dato por teclado y almacenarlo en la variable "dato"
print("Ingrese un nombre")
dato = input()
# 4. Si el valor de "dato" esta dentro de los valores de la variable "tupla", mostrar "si"
if(dato in tupla):
    print("si")
# 5. Si el valor de "dato" no esta dentro de los valores de la variale "tupla" mostar "no"
if(dato not in tupla):
    print("No")
