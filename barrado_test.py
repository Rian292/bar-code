import unittest
from barrado import buscar_barrado

class RegiaoTest(unittest.TestCase):
    def test_vendedor_barrado(self):
        resultado = buscar_barrado('584')
        self.assertTrue(resultado, True)    
    def test_vendedor_liberado(self):
        resultado = buscar_barrado('587')
        self.assertFalse(resultado, True)    
    

if __name__ == '__main__':
    unittest.main()
