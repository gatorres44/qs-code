import unittest
from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calculadora.somar(3, 4), 7)
        self.assertEqual(self.calculadora.somar(0, 0), 0)
        self.assertEqual(self.calculadora.somar(-5, 5), 0)

    def test_subtrair(self):
        self.assertEqual(self.calculadora.subtrair(8, 3), 5)
        self.assertEqual(self.calculadora.subtrair(0, 0), 0)
        self.assertEqual(self.calculadora.subtrair(-5, -3), -2)

    def test_multiplicar(self):
        self.assertEqual(self.calculadora.multiplicar(2, 3), 6)
        self.assertEqual(self.calculadora.multiplicar(0, 10), 0)
        self.assertEqual(self.calculadora.multiplicar(-4, -2), 8)

    def test_dividir(self):
        self.assertEqual(self.calculadora.dividir(10, 2), 5)
        self.assertEqual(self.calculadora.dividir(-6, 3), -2)
        self.assertRaises(ValueError, self.calculadora.dividir, 5, 0)

if __name__ == '__main__':
    unittest.main()