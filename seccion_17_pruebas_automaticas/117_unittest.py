#Unittest pruebas unitarias

def multiplicar(numero1, numero2):
    return numero1 * numero2

resuldado = multiplicar(2,4)
print(resuldado)



import unittest

class pruebas(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplicar(2,4),8)
        self.assertEqual(multiplicar(2,4),9)

if __name__ == '__main__':
    unittest.main()