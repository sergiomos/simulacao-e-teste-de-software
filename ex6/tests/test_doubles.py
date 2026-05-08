import sys
import os
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.calculadora import Calculadora


class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        # Stub: salvar() nao faz nada de verdade
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        # A calculadora pode ser testada mesmo antes do repositorio existir
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)

    def test_stub_aceita_qualquer_chamada(self):
        # Stub aceita salvar sem importar quantos valores
        for i in range(5):
            self.calc.somar(i, i)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)


class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_chamado_com_argumento_correto_subtracao(self):
        self.calc.subtrair(10, 4)
        self.mock_repo.salvar.assert_called_once_with("10 - 4 = 6")

    def test_mock_salvar_chamado_com_argumento_correto_multiplicacao(self):
        self.calc.multiplicar(3, 5)
        self.mock_repo.salvar.assert_called_once_with("3 * 5 = 15")

    def test_mock_salvar_chamado_com_argumento_correto_divisao(self):
        self.calc.dividir(8, 2)
        self.mock_repo.salvar.assert_called_once_with("8 / 2 = 4.0")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_salvar_nao_chamado_em_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)
        self.mock_repo.salvar.assert_not_called()


class TestBugPotencia(unittest.TestCase):
    """O mock revela o bug intencional: potencia registra '*' em vez de '**'."""

    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_revela_bug_em_potencia(self):
        self.calc.potencia(2, 3)
        # O argumento esperado seria "2 ** 3 = 8" mas o codigo registra com "*"
        self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")


if __name__ == "__main__":
    unittest.main()
