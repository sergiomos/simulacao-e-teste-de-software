from calculadora import somar, subtrair, multiplicar, dividir


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
