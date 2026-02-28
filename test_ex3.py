import pytest
from ex3 import calcular_frete, calcular_frete_base, calcular_acrescimo
from hypothesis import given, strategies as st

@pytest.fixture
def destinos_validos():
    return ["mesma região", "outra região"]

@pytest.fixture
def destinos_invalidos():
    return ["internacional", "", None]

@pytest.mark.parametrize("peso,destino,valor,esperado", [
    (0.5, "mesma região", 50, 10.0),
    (3, "outra região", 50, 22.5),
    (10, "mesma região", 50, 25.0),
    (2, "mesma região", 250, 0.0),
    (5, "outra região", 150, 22.5),
])
def test_classes_equivalencia(peso, destino, valor, esperado):
    assert calcular_frete(peso, destino, valor) == esperado

@pytest.mark.parametrize("peso,esperado_base", [
    (0.9, 10),
    (1.0, 10),
    (1.1, 15),
    (4.9, 15),
    (5.0, 15),
    (5.1, 25),
    (19.9, 25),
    (20.0, 25),
    (20.1, None),
])
def test_limites_peso(peso, esperado_base):
    if esperado_base is None:
        with pytest.raises(ValueError):
            calcular_frete_base(peso)
    else:
        assert calcular_frete_base(peso) == esperado_base

@pytest.mark.parametrize("peso,destino,esperado", [
    (0.5, "mesma região", 10.0),
    (0.5, "outra região", 15.0),
    (3,   "mesma região", 15.0),
    (3,   "outra região", 22.5),
    (10,  "mesma região", 25.0),
    (10,  "outra região", 37.5),
])
def test_tabela_decisao(peso, destino, esperado):
    assert calcular_frete(peso, destino, 100) == esperado


def test_peso_invalido_lanca_excecao():
    with pytest.raises(ValueError):
        calcular_frete(-1, "mesma região", 50)
    with pytest.raises(ValueError):
        calcular_frete(100, "mesma região", 50)

def test_destino_invalido_lanca_excecao(destinos_invalidos):
    for destino in destinos_invalidos:
        with pytest.raises(ValueError):
            calcular_frete(1, destino, 50)


destinos_strategy = st.sampled_from(["mesma região", "outra região"])

@given(
    peso=st.floats(min_value=0.01, max_value=20),
    destino=destinos_strategy,
    valor=st.floats(min_value=0, max_value=1000),
)
def test_frete_nao_negativo(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) >= 0


@given(
    peso=st.floats(min_value=0.01, max_value=20),
    destino=destinos_strategy,
    valor=st.floats(min_value=200.01, max_value=1000),
)
def test_frete_gratis_para_pedidos_acima_200(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) == 0.0


@given(
    peso=st.floats(min_value=0.01, max_value=20),
    valor=st.floats(min_value=0, max_value=1000),
)
def test_outra_regiao_maior_ou_igual_mesma(peso, valor):
    frete_mesma = calcular_frete(peso, "mesma região", valor)
    frete_outra = calcular_frete(peso, "outra região", valor)
    assert frete_outra >= frete_mesma
