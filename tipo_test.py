import unittest
from tipo import buscar_tipo, liberar_tipo

class BuscarTipoTest(unittest.TestCase):
    def test_joias(self):
        resultado = buscar_tipo('000')
        self.assertEqual(resultado, 'Jóias')
    def test_livros(self):
        resultado = buscar_tipo('111')
        self.assertEqual(resultado, 'Livros')
    def test_eletronicos(self):
        resultado = buscar_tipo('333')
        self.assertEqual(resultado, 'Eletrônicos')
    def test_bebidas(self):
        resultado = buscar_tipo('555')
        self.assertEqual(resultado, 'Bebidas')
    def test_brinquedos(self):
        resultado = buscar_tipo('888')
        self.assertEqual(resultado, 'Brinquedos')


class LiberarTipoTest(unittest.TestCase):    
    def test_vendedor_liberado(self):
        resultado = liberar_tipo('666')
        self.assertFalse(resultado, True) 


if __name__ == '__main__':
    unittest.main()
