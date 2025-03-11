# tkinter - componente label

import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#creamos el componente label (etiqueta)

texto = "Hola mundo"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg='green', bg='lightgrey', font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()

