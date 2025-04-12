from capa_datos.manejador_bd_sqlite import sqlite_connector as sqlite
from mvc.modelo.Tarea import tarea
from datetime import datetime

class tarea_controlador:

    def __init__(self):
        self.bd = sqlite()

    def crear_base_de_datos(self):
        nombre_de_base_de_datos = "tarea"
        self.bd.crear_la_base_de_datos(nombre_de_base_de_datos)

    def crear_tarea(self, descripcion, estado):
        db_sqlite = sqlite()
        fecha_creacion = datetime.now()
        db_sqlite.insertar_nueva_tarea(descripcion, estado, fecha_creacion, fecha_creacion)

    def modificar_tarea(self, id, descripcion, estado):
        tarea = self.buscar_tarea(id)
        tarea.descripcion = descripcion
        tarea.estado = estado
        tarea.fecha_actualizacion =datetime.now()
        db_sqlite = sqlite()
        db_sqlite.modificar_una_tarea(tarea)

    def eliminar_tarea(self, id):
        db_sqlite = sqlite()
        db_sqlite.eliminar_una_tarea(id)
        self.listar_tareas()

    def listar_tareas(self):
        db_sqlite = sqlite()
        lista = db_sqlite.listar_tareas()
        # for t in lista:
        #    print(t)
        return lista

    def buscar_tarea(self, id):
        db_sqlite = sqlite()
        tarea = db_sqlite.buscar_una_tarea(id)
        return tarea

    def crear_archivo_txt(self):
        pass