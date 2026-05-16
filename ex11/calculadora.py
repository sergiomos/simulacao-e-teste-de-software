"""
Modulo calculadora -- CC8550 CI/CD Lab
Funcoes matematicas basicas para uso didatico.
"""


def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtracao(a, b):
    """Retorna a diferenca entre a e b."""
    return a - b


def multiplicacao(a, b):
    """Retorna o produto de a e b."""
    return a * b


def divisao(a, b):
    """
    Retorna o quociente de a dividido por b.
    Lanca ValueError se b for zero.
    """
    if b == 0:
        raise ValueError("Divisao por zero nao e permitida.")
    return a / b


def percentual(valor, percent):
    """
    Retorna o valor correspondente ao percentual informado.
    Exemplo: percentual(200, 10) retorna 20.0
    Lanca ValueError se percent for negativo.
    """
    if percent < 0:
        raise ValueError("Percentual nao pode ser negativo.")
    return valor * percent / 100


def eh_par(n):
    """Retorna True se n for par, False caso contrario."""
    return n % 2 == 0
