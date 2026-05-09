# M1: troca operador + por - em somar.
def somar(a, b):
    return a - b


# M2: troca operador - por + em subtrair.
def subtrair(a, b):
    return a + b


# M3: troca operador * por + em multiplicar.
def multiplicar(a, b):
    return a + b


# M4: inverte a condicao do guard em dividir (== 0 -> != 0).
def dividir(a, b):
    if b != 0:
        raise ValueError("divisao por zero")
    return a / b


# M5: troca == por > em eh_par (n % 2 == 0 -> n % 2 > 0).
def eh_par(n):
    return n % 2 > 0
