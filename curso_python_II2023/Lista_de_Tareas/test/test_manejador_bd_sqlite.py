import unittest
from capa_datos.manejador_bd_sqlite import sqlite_connector as sql

class prueba(unittest.TestCase):

    def test(self):
        self.bd = sql()
        self.assertEqual(self.bd.crear_la_base_de_datos("prueba2023"),True)


if __name__ == '__main__':
    unittest.main()