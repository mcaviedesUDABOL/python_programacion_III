# tkinter - componente text

import tkinter

raiz = tkinter.Tk()

raiz.title("Mi programa")

#creamos el componente  text

entrada =  tkinter.Text(raiz)
entrada.config(width=20, height=10, font=("verdana",15), padx=10, pady=10, fg="green", selectbackground="lightgrey")
entrada.pack()


raiz.mainloop()
