import sys
import os
from platform import system

from termcolor import colored, cprint

class menu:

    def __init__(self):
        pass

    def __imprimir_menu(self):
        text = colored("Dime ¿Que opcion eliges?", "white", "on_blue", attrs=["bold"])
        print(text)
        text = colored("1) Insertar una nueva tarea", "green")
        print(text)
        text = colored("2) Modificar una nueva tarea", "green")
        print(text)
        text = colored("3) Eliminar una nueva tarea", "green")
        print(text)
        text = colored("4) Buscar una Tarea", "green")
        print(text)
        text = colored("5) Listar tareas", "green")
        print(text)
        text = colored("9) Salir ", "red")
        print(text)

    def __opciones(self, opcion):
        terminar = False
        if opcion == 1:
            print("crear")
        elif opcion == 2:
            print("modificar")
        elif opcion == 3:
            print("eliminar")
        elif opcion == 4:
            print("buscar")
        elif opcion == 5:
            print("listar")
        elif opcion == 9:
            terminar = True
        else:
            print("elija un numero del menu")
        return terminar

    def __validar_opcion_numero(self, opcion_cadena):
        opcion_convertida = -1
        if(opcion_cadena.isdigit() == True):
            opcion_convertida = int(opcion_cadena)
        return opcion_convertida

    def gestionar_menu(self):
        opcion = 0
        while True:
            os.system('cls')
            self.__imprimir_menu()
            opcion =0
            opcion_cadena = input("Elija una opcion: ")
            opcion = self.__validar_opcion_numero(opcion_cadena)
            if(opcion != -1):
                salir =self.__opciones(opcion)
                if(salir == True):
                    break
            else:
                print("Opción incorrecta")