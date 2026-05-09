import unittest

from calculadora import somar, subtrair, multiplicar, dividir, eh_par


class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_eh_par_true(self):
        self.assertTrue(eh_par(4))

    def test_eh_par_false(self):
        self.assertFalse(eh_par(5))


if __name__ == "__main__":
    unittest.main()
