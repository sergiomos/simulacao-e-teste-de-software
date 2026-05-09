"""Roda as mesmas asserções dos testes contra cada mutante e reporta
quem foi MORTO (teste falhou) ou SOBREVIVEU (teste passou)."""

import mutantes_manuais as m


def matou(funcao):
    """Retorna True se o teste falhou (mutante MORTO)."""
    try:
        funcao()
    except AssertionError:
        return True
    except Exception:
        return True
    return False


def t_m1():
    assert m.somar_m1(2, 3) == 5


def t_m2():
    assert m.subtrair_m2(10, 4) == 6


def t_m3():
    assert m.multiplicar_m3(3, 4) == 12


def t_m4():
    # esperado: dividir(10, 2) == 5 (sem excecao)
    assert m.dividir_m4(10, 2) == 5


def t_m5():
    assert m.eh_par_m5(4) is True


MUTANTES = [
    ("M1: somar (+ -> -)",       t_m1),
    ("M2: subtrair (- -> +)",    t_m2),
    ("M3: multiplicar (* -> +)", t_m3),
    ("M4: dividir (== -> !=)",   t_m4),
    ("M5: eh_par (== -> >)",     t_m5),
]


def main():
    print(f"{'Mutante':<32} | Status")
    print("-" * 50)
    mortos = 0
    for nome, teste in MUTANTES:
        if matou(teste):
            status = "MORTO"
            mortos += 1
        else:
            status = "SOBREVIVEU"
        print(f"{nome:<32} | {status}")
    total = len(MUTANTES)
    score = mortos / total * 100
    print(f"\nScore de mutacao: {mortos}/{total} ({score:.1f}%)")


if __name__ == "__main__":
    main()
