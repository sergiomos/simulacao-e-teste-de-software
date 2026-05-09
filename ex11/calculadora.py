def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("divisao por zero")
    return a / b


def potencia(base, expoente):
    return base ** expoente


def raiz_quadrada(x):
    if x < 0:
        raise ValueError("raiz de numero negativo")
    return x ** 0.5
