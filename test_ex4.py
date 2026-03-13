import pytest
from ex4 import *

@pytest.mark.parametrize("n, esperado", [
    (4, "Par positivo"),      # C1: n>0 e par
    (3, "Impar positivo"),    # C2: n>0 e ímpar
    (-5, "Negativo"),         # C3: n<0
    (0, "Zero"),              # C4: n==0
], ids=["par_positivo", "impar_positivo", "negativo", "zero"])
def test_verificar(n, esperado):
    assert verificar(n) == esperado


@pytest.mark.parametrize("x, esperado", [
    (150, "Alto"),    # C1: x>100 → ramo 2V
    (75, "Medio"),    # C2: 50<x≤100 → ramos 2F, 4V
    (30, "Baixo"),   # C3: x≤50 → ramos 2F, 4F
], ids=["alto", "medio", "baixo"])
def test_classificar(x, esperado):
    assert classificar(x) == esperado


@pytest.mark.parametrize("idade, membro, esperado", [
    (20, True, "Permitido"),   # CC1: idade>=18(V), membro(V)
    (20, False, "Negado"),     # CC2: idade>=18(V), membro(F)
    (15, True, "Negado"),      # CC3: idade>=18(F), curto-circuito
    (15, False, "Negado"),     # CC4: idade>=18(F), curto-circuito
], ids=["maior_e_membro", "maior_nao_membro", "menor_membro", "menor_nao_membro"])
def test_acesso(idade, membro, esperado):
    assert acesso(idade, membro) == esperado


@pytest.mark.parametrize("n, esperado", [
    (0, 0),    # Laço ignorado (0 iterações)
    (1, 0),    # Laço 1 vez (i=0)
    (5, 10),   # Laço várias vezes (0+1+2+3+4=10)
], ids=["zero_iteracoes", "uma_iteracao", "varias_iteracoes"])
def test_somar_ate(n, esperado):
    assert somar_ate(n) == esperado


@pytest.mark.parametrize("m, n, esperado", [
    (0, 0, 0),   # Ambos laços ignorados
    (2, 0, 0),   # Apenas laço j ignorado
    (1, 3, 3),   # i=1 vez, j=3 vezes → 1×3 prints
    (3, 3, 9),   # Ambos várias vezes → 3×3 prints
], ids=["ambos_ignorados", "j_ignorado", "i1_j3", "i3_j3"])
def test_percorrer_matriz(m, n, esperado):
    assert percorrer_matriz(m, n) == esperado


@pytest.mark.parametrize("numeros, esperado", [
    ([], "Abaixo"),        # Laço 0 iterações
    ([4], "Abaixo"),       # n>0 par, total=4 ≤10
    ([-1], "Abaixo"),      # n<0, total=-1 ≤10
    ([3], "Abaixo"),       # n>0 ímpar → continue
    ([0], "Abaixo"),       # n=0 → continue (else)
    ([12], "Acima"),       # n>0 par, total=12 >10
    ([4, 8], "Acima"),     # Várias iterações, total=12 >10
], ids=["vazio", "par_abaixo", "negativo", "impar_continue", "zero_continue", "par_acima", "varias_iter"])
def test_analisar(numeros, esperado):
    assert analisar(numeros) == esperado


@pytest.mark.parametrize("preco, cliente_vip, esperado", [
    (100, True, 80),     # VIP, total=80 ≥50
    (100, False, 100),   # Não VIP, total=100 ≥50
    (40, False, 50),     # Não VIP, total=40 <50 → total=50
    (50, True, 50),      # VIP, desc=10, total=40 <50 → total=50
], ids=["vip_sem_minimo", "nao_vip_sem_minimo", "nao_vip_com_minimo", "vip_com_minimo"])
def test_desconto(preco, cliente_vip, esperado):
    assert desconto(preco, cliente_vip) == esperado
