import pytest

from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    raiz_quadrada,
)


def test_somar():
    assert somar(2, 3) == 5


def test_somar_negativos():
    assert somar(-2, -3) == -5


def test_subtrair():
    assert subtrair(10, 4) == 6


def test_subtrair_resultado_negativo():
    assert subtrair(2, 5) == -3


def test_multiplicar():
    assert multiplicar(6, 7) == 42


def test_multiplicar_por_zero():
    assert multiplicar(99, 0) == 0


def test_dividir_basico():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_potencia():
    assert potencia(2, 10) == 1024


def test_potencia_expoente_zero():
    assert potencia(7, 0) == 1


def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3


def test_raiz_quadrada_zero():
    assert raiz_quadrada(0) == 0


def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)
