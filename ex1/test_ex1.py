import pytest
from ex1 import *

@pytest.mark.parametrize("nota,esperado", [
    (0, True),
    (5, True),
    (10, True),
    (-1, False),
    (11, False),
])
def test_validar_nota(nota, esperado):
    assert validar_nota(nota) == esperado

@pytest.mark.parametrize("notas,esperado", [
    ([7, 8, 9], 8),
    ([7, 8, 15, -3], 7.5),
    ([10], 10),
])
def test_calcular_media_valida(notas, esperado):
    assert calcular_media(notas) == esperado

def test_calcular_media_lista_vazia():
    with pytest.raises(ValueError, match="Não há notas para calcular a média"):
        calcular_media([])


def test_calcular_media_todas_invalidas():
    # Nenhuma nota válida → divisão por zero
    with pytest.raises(ZeroDivisionError):
        calcular_media([-5, 20])


@pytest.mark.parametrize("media,esperado", [
    (7, "APROVADO"),
    (10, "APROVADO"),
    (5, "RECUPERAÇÃO"),
    (6.9, "RECUPERAÇÃO"),
    (0, "REPROVADO"),
    (4.9, "REPROVADO"),
])
def test_obter_situacao_valida(media, esperado):
    assert obter_situacao(media) == esperado


@pytest.mark.parametrize("media", [-1, 11])
def test_obter_situacao_invalida(media):
    with pytest.raises(ValueError, match="Média inválida"):
        obter_situacao(media)

def test_calcular_estatisticas():
    notas = [8, 6, 4, 9]

    resultado = calcular_estatisticas(notas)

    assert resultado == {
        "media": 6.75,
        "maior": 9,
        "menor": 4,
        "aprovados": 2,
        "reprovados": 1,
        "recuperacao": 1
    }

@pytest.mark.parametrize("notas,nota_maxima,esperado", [
    ([5, 10], 20, [10, 20]),
    ([0, 10], 100, [0, 100]),
    ([], 50, []),
])
def test_normalizar_nota(notas, nota_maxima, esperado):
    assert normalizar_nota(notas, nota_maxima) == esperado
