# mostrar mensaje messagebox para realizar preguntas

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
    tkinter.messagebox.askquestion("Titulo de la pregunta","Quieres borrar este fichero?")

boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=avisar)
boton.pack()

raiz.mainloop()
