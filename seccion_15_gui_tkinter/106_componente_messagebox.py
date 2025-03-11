# mostrar mensaje messagebox (mostrar informacion)

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
    tkinter.messagebox.showinfo("Titulo","Mensaje con la informacion")

boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()

raiz.mainloop()

