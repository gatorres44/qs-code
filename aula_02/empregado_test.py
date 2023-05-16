import unittest
from empregado import Empregado

class TestEmpregado(unittest.TestCase):
    def setUp(self):
        self.empregado = Empregado("João", "Silva", "gerente", 5000)

    def test_calcular_reajuste(self):
        self.assertEqual(self.empregado.calcular_reajuste(), 5250.0)

    def test_gerar_nome_completo(self):
        self.assertEqual(self.empregado.gerar_nome_completo(), "João Silva")

    def test_validar_cargo(self):
        self.assertTrue(self.empregado.validar_cargo())

        self.empregado.cargo = "estagiário"
        self.assertFalse(self.empregado.validar_cargo())

if __name__ == '__main__':
    unittest.main()
