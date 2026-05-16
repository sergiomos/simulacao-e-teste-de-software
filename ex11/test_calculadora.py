"""
Testes para o modulo calculadora.
ATENCAO: esta suite esta incompleta -- a cobertura atual e de ~65%.
O pipeline de CI ira falhar na etapa de cobertura (minimo exigido: 80%).
Sua tarefa: identificar as funcoes nao cobertas e escrever os testes
que faltam ate o pipeline ficar verde.
"""

import pytest
from calculadora import soma, subtracao, multiplicacao, divisao, percentual, eh_par


# ----------------------------------------------------------------
# soma
# ----------------------------------------------------------------

def test_soma_inteiros_positivos():
    assert soma(3, 4) == 7


def test_soma_com_numero_negativo():
    assert soma(-1, 5) == 4


def test_soma_dois_negativos():
    assert soma(-2, -3) == -5

def test_soma_com_zero():
    assert soma(10, 0) == 10

def test_soma_com_nao_inteiro():
    assert soma(3.5, 2.5) == 6.0


# ----------------------------------------------------------------
# subtracao
# ----------------------------------------------------------------

def test_subtracao_resultado_positivo():
    assert subtracao(10, 3) == 7


def test_subtracao_resultado_negativo():
    assert subtracao(2, 8) == -6

def test_subtracao_com_zero():
    assert subtracao(5, 0) == 5

def test_subtracao_com_nao_inteiro():
    assert subtracao(5.5, 2.0) == 3.5


# ----------------------------------------------------------------
# multiplicacao
# ----------------------------------------------------------------

def test_multiplicacao_inteiros():
    assert multiplicacao(4, 5) == 20


def test_multiplicacao_por_zero():
    assert multiplicacao(7, 0) == 0


def test_multiplicacao_negativos():
    assert multiplicacao(-3, -4) == 12

def test_multiplicacao_com_nao_inteiro():
    assert multiplicacao(2.5, 4) == 10.0


# ----------------------------------------------------------------
# divisao -- INCOMPLETA: faltam casos importantes
# ----------------------------------------------------------------

def test_divisao_resultado_exato():
    assert divisao(10, 2) == 5.0


def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)


def test_divisao_resultado_nao_inteiro():
    assert divisao(7, 2) == 3.5


# ----------------------------------------------------------------
# percentual -- NAO COBERTA
# ----------------------------------------------------------------

def test_percentual_valor_positivo():
    assert percentual(200, 10) == 20.0

def test_percentual_valor_negativo():
    assert percentual(-100, 20) == -20.0


# ----------------------------------------------------------------
# eh_par -- NAO COBERTA
# ----------------------------------------------------------------

def test_eh_par_numero_par():
    assert eh_par(4) is True

def test_eh_par_numero_impar():
    assert eh_par(7) is False
