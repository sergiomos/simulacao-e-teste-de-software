import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.calculadora import Calculadora


class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_soma_retorna_valor_correto(self):
        self.assertEqual(self.calc.somar(5, 3), 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_subtracao_retorna_valor_correto(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_subtracao_resultado_negativo(self):
        self.assertEqual(self.calc.subtrair(2, 5), -3)

    def test_multiplicacao_retorna_valor_correto(self):
        self.assertEqual(self.calc.multiplicar(6, 7), 42)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(self.calc.multiplicar(99, 0), 0)

    def test_divisao_retorna_valor_correto(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_divisao_resultado_fracionario(self):
        self.assertAlmostEqual(self.calc.dividir(1, 3), 0.3333333, places=5)

    def test_potencia_retorna_valor_correto(self):
        self.assertEqual(self.calc.potencia(2, 10), 1024)

    def test_potencia_expoente_zero(self):
        self.assertEqual(self.calc.potencia(7, 0), 1)


class TestTipagem(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_tipagem_string_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_tipagem_none_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

    def test_tipagem_lista_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair([1], 1)

    def test_tipagem_string_em_multiplicacao(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar(2, "x")

    def test_tipagem_dict_em_potencia(self):
        with self.assertRaises(TypeError):
            self.calc.potencia({}, 2)

    def test_tipagem_bool_e_aceito(self):
        # bool e subclasse de int em Python; comportamento esperado: aceita.
        self.assertEqual(self.calc.somar(True, 1), 2)


class TestLimites(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        self.assertFalse(resultado == float("inf"))

    def test_divisao_por_numero_muito_pequeno(self):
        resultado = self.calc.dividir(1, 1e-300)
        self.assertGreater(resultado, 0)

    def test_potencia_expoente_negativo(self):
        self.assertAlmostEqual(self.calc.potencia(2, -2), 0.25)

    def test_potencia_expoente_fracionario(self):
        self.assertAlmostEqual(self.calc.potencia(9, 0.5), 3.0)


class TestForaDoIntervalo(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


class TestMensagensDeErro(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)


class TestFluxosDeControle(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_caminho_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_caminho_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_caminho_validacao_tipo(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar("a", 2)


if __name__ == "__main__":
    unittest.main()
