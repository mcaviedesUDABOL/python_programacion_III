from mvc.controlador.Tarea_controlador import tarea_controlador as t_c
from mvc.modelo.Tarea import tarea as t

class tarea_vista:

    """
        Clase de Vista tarea muestra metodos que permiten ver la
        informacion de las tareas pedidas al controlador tarea
    """

    def __init__(self):
       """
            Constructor de la vista tarea
        :param self: Una llamada a la instancia del objeto
        :return: No retorna nada
       """
       self.__tarea_c = t_c()

    def crear_base_de_datos_por_defecto(self):
        """
            Metodo para la creacion de la base de datos
        :return: No returna nada
        """
        self.__tarea_c.crear_base_de_datos()

    def insertar_nueva_tarea(self):
        descripcion = input("Ingresa la descripción de la tarea: ")
        estado =int(input("Ingresa el estado de la tarea 1) EN_ESPERA, 2) INICADO y 3) TERMINADO: "))
        self.__tarea_c.crear_tarea(descripcion, estado)

    def ver_tareas(self):
        lista_tareas = self.__tarea_c.listar_tareas()
        for tarea in lista_tareas:
            print(tarea)

    def buscar_una_tarea(self):
        id_cadena = input("Ingrese el identificador de la tarea: ")
        id = int(id_cadena)
        tarea = self.__tarea_c.buscar_tarea(id)
        print(tarea)

    def modificar_una_tarea(self):
        self.ver_tareas()
        id = input("Elije el identificador: ")
        descripcion = input("Ingresa la descripción de la tarea: ")
        estado = int(input("Ingresa el estado de la tarea 1) EN_ESPERA, 2) INICADO y 3) TERMINADO: "))
        self.__tarea_c.modificar_tarea(id,descripcion,estado)

    def eliminar_una_tarea(self):
        self.ver_tareas()
        id = input("Elije el identificador: ")
        self.__tarea_c.eliminar_tarea(id)

    def crear_archivo(self):
        lista_tareas = self.__tarea_c.listar_tareas()

