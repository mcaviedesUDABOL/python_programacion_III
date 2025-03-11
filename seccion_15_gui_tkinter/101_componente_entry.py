# tkinter - componente entry

import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")


entrada = tkinter.Entry(raiz)
entrada.config(justify="center")
#entrada.config(justify="center", show="*")
entrada.pack()

raiz.mainloop()
