# grabar un fichero de texto

fichero = open("c:\\Users\\mento\\Desktop\\curso_python\\seccion_17\\fichero_para_grabar.txt","wt")

texto = "esta es la linea que se va agrabar en el fichero"

fichero.write(texto)

fichero.close()

