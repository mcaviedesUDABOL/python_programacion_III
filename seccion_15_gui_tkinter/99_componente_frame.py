# tkinter - componente frame

import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#creamos el componente Frame

frame = tkinter.Frame(raiz)
frame.config(bg="blue", width = 400, height = 300)
frame.pack()

raiz.mainloop()

