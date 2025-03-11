# agregar al fichero nuevas lineas

fichero = open("c:\\Users\\mento\\Desktop\\curso_python\\seccion_17\\ficherotexto.txt","at")
incluir = "\n Esta es una tercera fila del fichero"

fichero.write(incluir)

fichero.close()