from mvc.vista.Tarea_vista import tarea_vista as t_v
from mvc.modelo.Tarea import tarea as t

class menu:

    def __init__(self):
        self.__tarea_v = t_v()

    def mostrar_menu(self):

        opcion = 0
        while True:
            print("""
                Dime, ¿Qué opción eliges?
                1) Insertar una nueva Tarea
                2) Modificar una nueva Tarea
                3) Eliminar una nueva Tarea
                4) Buscar una Tarea
                5) Listar tareas
                6) Crear la base de datos
                7) Crear un archivo txt con la lista de tareas
                8) Salir de la aplicación
                0) Ayuda
            """)
            opcion = 0
            opcion_cadena = input("Elige una opción: ")
            if(opcion_cadena.isdigit() == True):
                opcion = int(opcion_cadena)
                if opcion == 1:
                    self.__tarea_v.insertar_nueva_tarea()
                elif opcion ==2:
                    self.__tarea_v.modificar_una_tarea()
                elif opcion == 3:
                    self.__tarea_v.eliminar_una_tarea()
                elif opcion == 4:
                    self.__tarea_v.buscar_una_tarea()
                elif opcion==5:
                    self.__tarea_v.ver_tareas()
                elif opcion==6:
                    self.__tarea_v.crear_base_de_datos_por_defecto()
                elif opcion==7:
                    self.__tarea_v.crear_archivo()
                elif opcion ==8:
                    break
                elif opcion >=9:
                    print("Opción incorrecta")
                elif opcion ==0:
                    help(self.__tarea_v)
                    help(t)
            else:
                print("Opción incorrecta")