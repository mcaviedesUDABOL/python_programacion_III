import modulofichero

nombre_fichero = 'fichero.txt'
direccion = 'c:\\Users\\mento\\Desktop\\curso_python\\seccion_17\\'
direccion_fichero = direccion + nombre_fichero
fichero = modulofichero.fichero(direccion_fichero)

texto = 'Esta es la primera fila del fichero.\n Esta sera la segunda fila.'
fichero.grabar_fichero(texto)


texto = '\nEste es un texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)
