#hacer una calculadora parte 01
#
#from tkinter import *
import tkinter as tk
#from tkinter import ttk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("385x500")
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

def pulsar(valor):
    global operacion
    global resultado
    operacion = operacion + str(valor)
    pantalla.delete(0,tk.END)
    pantalla.insert(0, operacion)


#creacion del Display de los resultados
pantalla = tk.Entry(ventana, font=("arial",20,"bold"), borderwidth=2)
pantalla.grid(row=0,column=0,columnspan=3, pady=1, padx=1)

#Creacion de reiniciar operaciones
boton_reset = tk.Button(ventana, text="AC", width=8, height=2, command=lambda:borrar())
boton_reset.grid(row=0, column=3, pady=1)

ancho = 8
alto = 3
#botones de la primera fila
boton7 = tk.Button(ventana, text="7", width = ancho, height = alto, command=lambda:pulsar("7"))
boton7.grid(row = 1, column=0)

boton8 = tk.Button(ventana, text="8", width = ancho, height = alto, command=lambda:pulsar("8"))
boton8.grid(row = 1, column=1)

boton9 = tk.Button(ventana, text="9", width = ancho, height = alto, command=lambda:pulsar("9"))
boton9.grid(row = 1, column=2)

boton_div = tk.Button(ventana, text="/", width = ancho, height = alto, command=lambda:pulsar("/"))
boton_div.grid(row = 1, column=3)

ventana.mainloop()