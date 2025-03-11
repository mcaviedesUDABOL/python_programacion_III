# filedialog para abir un archivo

import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

#definir archivo
def abrirArchivo():
    rutaFichero = filedialog.askopenfile(title ="Abrir fichero")
    print(rutaFichero)

boton = tkinter.Button(raiz, text="Pulsar para empezar", command=abrirArchivo)
boton.pack()

raiz.mainloop()
