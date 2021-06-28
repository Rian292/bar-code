import unittest
from regiao import buscar_regiao

class RegiaoTest(unittest.TestCase):
    def test_centro_oeste(self):
        resultado = buscar_regiao('111')
        self.assertEqual(resultado, 'Centro-oeste')    
    
    def test_nordeste(self):
        resultado = buscar_regiao('333')
        self.assertEqual(resultado, 'Nordeste')

    def test_norte(self):
        resultado = buscar_regiao('555')
        self.assertEqual(resultado, 'Norte')
   
    def test_sul(self):
        resultado = buscar_regiao('000')
        self.assertEqual(resultado, 'Sul')


if __name__ == '__main__':
    unittest.main()
