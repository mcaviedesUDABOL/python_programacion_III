#hacer una calculadora parte 01
#
#from tkinter import *
import tkinter as tk
#from tkinter import ttk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("385x280")
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

def calcular():
    global operacion
    global resultado
    try: 
        resultado = str(eval(operacion))
    except:
        resultado = "Error"
    finally:
        pantalla.delete(0, tk.END)
        pantalla.insert(0,resultado)

#creacion del Display de los resultado
pantalla = tk.Entry(ventana, font=("arial",20,"bold"), borderwidth=2)
pantalla.config(justify="right")
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

#botones de la segunda fila
boton4 = tk.Button(ventana, text="4", width = ancho, height = alto, command=lambda:pulsar("4"))
boton4.grid(row = 2, column=0)

boton5 = tk.Button(ventana, text="5", width = ancho, height = alto, command=lambda:pulsar("5"))
boton5.grid(row = 2, column=1)

boton6 = tk.Button(ventana, text="6", width = ancho, height = alto, command=lambda:pulsar("6"))
boton6.grid(row = 2, column=2)

boton_pro = tk.Button(ventana, text="*", width = ancho, height = alto, command=lambda:pulsar("*"))
boton_pro.grid(row = 2, column=3)

#botones de la tercera fila
boton1 = tk.Button(ventana, text="1", width = ancho, height = alto, command=lambda:pulsar("1"))
boton1.grid(row = 3, column=0)

boton2 = tk.Button(ventana, text="2", width = ancho, height = alto, command=lambda:pulsar("2"))
boton2.grid(row = 3, column=1)

boton3 = tk.Button(ventana, text="3", width = ancho, height = alto, command=lambda:pulsar("3"))
boton3.grid(row = 3, column=2)

boton_minor = tk.Button(ventana, text="-", width = ancho, height = alto, command=lambda:pulsar("-"))
boton_minor.grid(row = 3, column=3)

#botones de la cuearta fila
boton_com = tk.Button(ventana, text=".", width = ancho, height = alto, command=lambda:pulsar("."))
boton_com.grid(row = 4, column=0)

boton0 = tk.Button(ventana, text="0", width = ancho, height = alto, command=lambda:pulsar("0"))
boton0.grid(row = 4, column=1)

boton_igu = tk.Button(ventana, text="=", width = ancho, height = alto, command=lambda:calcular())
boton_igu.grid(row = 4, column=2)

boton_plus = tk.Button(ventana, text="+", width = ancho, height = alto, command=lambda:pulsar("+"))
boton_plus.grid(row = 4, column=3)

ventana.mainloop()