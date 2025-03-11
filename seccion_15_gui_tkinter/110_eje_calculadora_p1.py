#hacer una calculadora parte 01
#
#from tkinter import *
import tkinter as tk
#from tkinter import ttk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("390x600")
ventana.resizable(False,False)
ventana.configure(background="gray")

#funciones
operacion = ""
resultado =  tk.StringVar()

def borrar():
    global operacion
    global resultado
    operacion = ""
    pantalla.delete(0, tk.END)

#creacion del Display de los resultados
pantalla = tk.Entry(ventana, font=("arial",20,"bold"), borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3, pady=10, padx=5)

#Creacion de reiniciar operaciones
boton_reset = tk.Button(ventana, text="AC", width=8, height=2, command=lambda:borrar())
boton_reset.grid(row=0, column=3, pady=5)



ventana.mainloop()