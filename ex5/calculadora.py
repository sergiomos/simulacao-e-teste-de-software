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


def eh_par(n):
    return n % 2 == 0
