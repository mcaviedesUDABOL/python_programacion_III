import sqlite3
import datetime
from mvc.modelo.Tarea import tarea
import pathlib
import logging
from datetime import datetime
from os import remove

class sqlite_connector:

    """
        Clase de conexion a la base de datos contiene el CRUD para la gestion de la base de datos

    >>> nombre_bd = "bd_tarea"
    >>> dir = pathlib.Path(__file__).parent.absolute().__str__()
    >>> direccion = "base_de_datos\\prueba.db"
    >>> remove(direccion)
    >>> sql = sqlite_connector("prueba")
    >>> sql.crear_la_base_de_datos()
    E:\\curso_python_II2023\\Lista_de_Tareas\\capa_datos\\base_de_datos\\prueba.db
    True
    >>> date_str = '2023-02-28 14:30:00'
    >>> date_str_2 = '2023-03-30 15:00:00'
    >>> date_format = '%Y-%m-%d %H:%M:%S'
    >>> fecha =  datetime.strptime(date_str, date_format)
    >>> fecha_2 =  datetime.strptime(date_str_2, date_format)
    >>> sql.insertar_nueva_tarea("prueba",1,fecha,fecha_2)
    1
    """

    def __init__(self):
        try:
            self.__nombre_bd = "bd_tarea"
            dir = pathlib.Path(__file__).parent.absolute().__str__()
            self.__direccion = dir + "\\base_de_datos\\{}.db".format(self.__nombre_bd)
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            logging.error(error)

    def __init__(self, nombre_db):
        try:
            self.__nombre_bd = nombre_db
            dir = pathlib.Path(__file__).parent.absolute().__str__()
            self.__direccion = dir + "\\base_de_datos\\{}.db".format(self.__nombre_bd)
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            logging.error(error)


    def crear_la_base_de_datos(self):
        """
            Este metodo sirve para la creacion de la base de datos
        :return: True
        """
        resultado = False
        try:
            print(self.__direccion)
            self.__conexion = sqlite3.connect(self.__direccion)
            self.__cursor = self.__conexion.cursor()
            slq_sentencia = ("DROP TABLE IF EXISTS '{nombre_bd}';".format(nombre_bd = self.__nombre_bd))
            self.__cursor.execute(slq_sentencia)
            slq_sentencia = (
                "CREATE TABLE 'tareas' ('id' INTEGER, 'descripcion'	"
                "TEXT, 'estado'	INTEGER, 'fecha_creacion' TEXT, "
                "'fecha_actualizacion_ultima' TEXT, PRIMARY KEY('id' AUTOINCREMENT) );".format(nombre_bd = self.__nombre_bd))
            self.__cursor.execute(slq_sentencia)
            self.__conexion.commit()
            self.__conexion.close()
            resultado = True
            return resultado
        except sqlite3.OperationalError as error:
            print("Error al abrir: ", error)
            self.__conexion.close()
            logging.error(error)
            return resultado

    def insertar_nueva_tarea(self, descripcion, estado, fecha_creacion, fecha_actualizacion):
        """
            Metodo que permite ingresar una nueva tarea en la base de datos
        :param descripcion: Descrpcion de la tarea
        :param estado: que estado tiene la tarea 1) EN_ESPERA, 2) INICADO y 3) TERMINADO
        :param fecha_creacion: fecha de la creacion de la tarea
        :param fecha_actualizacion: fecha de la ultima actualización de la tarea
        :return: Devuelve el ultimo identificador de la fila insertada
        """
        self.__conexion = None
        try:
            self.__conexion = sqlite3.connect(self.__direccion)
            self.__cursor = self.__conexion.cursor()
            slq_sentencia = (
                "insert into tareas values({i},'{d}',{e},'{f_c}','{f_a}');".format(i='null', d=descripcion, e=estado,
                                                                                   f_c=fecha_creacion,
                                                                                   f_a=fecha_actualizacion))
            #print(slq_sentencia)
            self.__cursor.execute(slq_sentencia)
            self.__conexion.commit()
            ultimo_id = self.__cursor.lastrowid
            self.__conexion.close()
            return ultimo_id
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            self.__conexion.close()
            return 0

    def modificar_una_tarea(self, tarea):
        """

        :param tarea:
        :return:
        """
        try:
            self.__conexion = sqlite3.connect(self.__direccion)
            self.__cursor = self.__conexion.cursor()
            slq_sentencia = (
                "UPDATE tareas SET descripcion='{d}', estado={e}, fecha_creacion='{f_c}', fecha_actualizacion_ultima='{f_a}'  WHERE id = {i};".format(
                    d=tarea.descripcion,
                    e=tarea.estado,
                    f_c=tarea.fecha_creacion,
                    f_a=tarea.fecha_actualizacion,
                    i= tarea.id
                    )
            )
            print(slq_sentencia)
            self.__cursor.execute(slq_sentencia)
            self.__conexion.commit()
            self.__conexion.close()
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            self.__conexion.close()

    def eliminar_una_tarea(self, id):
        """

        :param id:
        :return:
        """
        try:
            self.__conexion = sqlite3.connect(self.__direccion)
            self.__cursor = self.__conexion.cursor()
            slq_sentencia = ("delete from tareas where id = {i}".format(i=id))
            self.__cursor.execute(slq_sentencia)
            self.__conexion.commit()
            self.__conexion.close()
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            self.__conexion.close()

    def buscar_una_tarea(self, id):
        """

        :param id:
        :return:
        """
        try:
            self.__conexion = sqlite3.connect(self.__direccion)
            self.__cursor = self.__conexion.cursor()
            slq_sentencia = ("select * from tareas where id = {i}".format(i=id))
            self.__cursor.execute(slq_sentencia)
            tarea_lista = self.__cursor.fetchall()
            self.__conexion.close()
            if (len(tarea_lista) == 1):
                for tarea_bd in tarea_lista:
                    t = tarea(tarea_bd[0], tarea_bd[1], tarea_bd[2], tarea_bd[3], tarea_bd[4])
            return t
        except sqlite3.OperationalError as error:
            print("Error: ", error)
            self.__conexion.close()

    def listar_tareas(self):
        """

        :return:
        """
        try:
            self.__conexion = sqlite3.connect(self.__direccion)
            self.__cursor = self.__conexion.cursor()
            slq_sentencia = ("select * from tareas")
            self.__cursor.execute(slq_sentencia)
            tareas_base_datos = self.__cursor.fetchall()
            lista = []
            t = tarea
            for tarea_bd in tareas_base_datos:
                t = tarea(tarea_bd[0], tarea_bd[1], tarea_bd[2], tarea_bd[3], tarea_bd[4])
                # print(t)
                lista.append(t)
            self.__conexion.close()
            return lista
        except sqlite3.OperationalError as error:
            print("Error: ", error)


if __name__ == '__main__':
    import doctest
    doctest.testmod()