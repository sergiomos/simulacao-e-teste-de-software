"""Versoes mutadas de calculadora.py para teste de mutacao manual.

Cada mutante e uma copia de uma funcao original com UMA pequena alteracao,
o tipo de mutacao mais comum (operador trocado, condicao invertida).
"""


# M1: troca operador + por - em somar.
def somar_m1(a, b):
    return a - b


# M2: troca operador - por + em subtrair.
def subtrair_m2(a, b):
    return a + b


# M3: troca operador * por + em multiplicar.
def multiplicar_m3(a, b):
    return a + b


# M4: inverte a condicao do guard em dividir (== 0 -> != 0).
def dividir_m4(a, b):
    if b != 0:
        raise ValueError("divisao por zero")
    return a / b


# M5: troca == por > em eh_par (n % 2 == 0 -> n % 2 > 0).
def eh_par_m5(n):
    return n % 2 > 0
