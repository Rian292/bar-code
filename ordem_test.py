import unittest
from ordem import ordem

class OrdemTest(unittest.TestCase):
    def test_ordem(self):
        resultado = ordem('888333555999000')

        self.assertEquals(resultado[0], '888')
        self.assertEquals(resultado[1], '333')
        self.assertEquals(resultado[2], '555')
        self.assertEquals(resultado[3], '999')
        self.assertEquals(resultado[4], '000')


if __name__ == '__main__':
    unittest.main()