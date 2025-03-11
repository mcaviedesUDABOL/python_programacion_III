# tkinter - componente label

import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#creamos el componente button

def accion():
    print("Hola Mundo")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()



raiz.mainloop()
