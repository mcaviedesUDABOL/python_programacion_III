from datetime import datetime

class tarea:

    """
        Clase Tarea en esta clase contine todos los atributos de una tarea
        como ser identificador, descipcion, estado, fecha de creacion, fecha de la ultima actualizacion

    >>> date_str = '2023-02-28 14:30:00'
    >>> date_str_2 = '2023-03-30 15:00:00'
    >>> date_format = '%Y-%m-%d %H:%M:%S'
    >>> fecha =  datetime.strptime(date_str, date_format)
    >>> fecha_2 =  datetime.strptime(date_str_2, date_format)
    >>> t = tarea(1,"prueba",1,fecha,fecha_2)
    >>> t.id
    1
    >>> t.descripcion
    'prueba'
    >>> t.estado
    1
    >>> t.fecha_creacion
    datetime.datetime(2023, 2, 28, 14, 30)
    >>> t.fecha_actualizacion
    datetime.datetime(2023, 3, 30, 15, 0)

    """
    __fecha_creacion = datetime.now()
    __fecha_actualizacion = datetime.now()
    __id_tarea =0

    def __init__(self):
        """
            Construtor por defecto
        """
        self.__descripcion = ""
        self.__estado = ""

    def __init__(self, descripcion, estado):
        """
            Construtor por sobrecargado con descripcion y estado
        """
        self.__descripcion = descripcion
        self._estado = estado

    def __init__(self, id, descipcion, estado, fecha_creacion, fecha_actualizacion):
        """
            Construtor por sobrecargado con descripcion, estado, fecha de creacion, fecha de actualizacion
        """
        self.__id_tarea = id
        self.__descripcion = descipcion
        self._estado = estado
        self.__fecha_creacion = fecha_creacion
        self.__fecha_actualizacion = fecha_actualizacion

    @property
    def fecha_creacion(self):
        """
            Propiedad de fecha creacion mostrar valor
        :return: fecha creacion
        """
        return self.__fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, valor):
        """
            Propiedad fehca creacion cambiar valor
        :param valor: Valoer de la nueva fecha de creacion
        :return: No retorna nada
        """
        self.__fecha_creacion = valor

    @property
    def fecha_actualizacion(self):
        return self.__fecha_actualizacion

    @fecha_actualizacion.setter
    def fecha_actualizacion(self, valor = datetime.now() ):
        print(type(valor))
        self.__fecha_actualizacion = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def id(self):
        return self.__id_tarea

    def __str__(self):
        """
            Metedo por defecto que devuelve una cadena con los valores de los atributos de la clase
        :return: cadena con valores de los atributos
        """
        cadena = "La tarea es: Identificador: {i}, descripcion: {d}, estado: {e}, creacion {f_c}, actualizacion: {f_a}".format(
            i=self.__id_tarea, d=self.__descripcion, e=self._estado, f_c=self.__fecha_creacion,
            f_a=self.fecha_actualizacion)
        return cadena

    def __eq__(self, tarea):
        if (self.id == tarea.get_id):
            return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()