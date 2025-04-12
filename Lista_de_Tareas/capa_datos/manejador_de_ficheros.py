import pathlib
import os
import sys
from datetime import datetime

class manejador_ficheros():

    def __init__(self):
        dir = pathlib.Path(__file__).parent.absolute().__str__()
        nombre_fichero = "\\ficheros\\lista_tareas-{fecha}.txt".format(fecha = datetime.now())
        self.__fichero_direccion = dir+nombre_fichero

    def grabar_fichero(self, texto):
        try:
            self.__fichero = open(self.__fichero_direccion, "wt")
            self.__fichero.write(texto)
            self.__fichero.close()
        except OSError as err:
            print("OS error:", err)
            self.__fichero.close()
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.__fichero.close()

    def leer_fichero(self):
        try:
            self.__fichero = open(self.__fichero_direccion, "rt")
            datos_fichero = self.__fichero.read()
            self.__fichero.close()
            return datos_fichero
        except OSError as err:
            print("OS error:", err)
            self.__fichero.close()
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.__fichero.close()

    def incluir_datos_ficheros(self,texto):
        try:
            self.__fichero = open(self.__fichero_direccion, "at")
            self.__fichero.write(texto)
            self.__fichero.close()
        except OSError as err:
            print("OS error:", err)
            self.__fichero.close()
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            self.__fichero.close()

    def borrar_fichero(self):
        try:
            os.remove(self.__fichero_direccion)
        except OSError as err:
            print("OS error:", err)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")


