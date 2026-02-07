import pytest
from ex1 import *

@pytest.mark.parametrize("nota, esperado", [
    (2, True),
    (10, True),
    (0, True),
    (-2, False),
    (-2.43, False),
    (11, False),
    (2.34, True)])

def test_validar_nota(nota, esperado):
    assert validar_nota(nota) == esperado

@pytest.mark.parametrize("media, esperado", [
    (2, "REPROVADO"),
    (5, "RECUPERAÇÃO"),
    (7, "APROVADO"),
    (6, "RECUPERAÇÃO"),
    (5.1, "RECUPERAÇÃO"),
    (10, "APROVADO"),
    (0, "REPROVADO"),
    (4, "REPROVADO"),
   ])

def test_obter_situacao_sucesso(media, esperado):
    assert obter_situacao(media) == esperado

@pytest.mark.parametrize("media", [
    (-1),
    (20),
    (10.1),
    (-4.3)
   ])    

def test_obter_situacao_invalida(media):
    """Testa excecao com valores invalidos"""
    with pytest.raises(ValueError):
        obter_situacao(media)

@pytest.mark.parametrize("notas, esperado", [
    ([10, 10, 10, 10], 10),
    ([2, 4, 5, 6, 1, 10], 4.666666666666667),
    ([20, 30, 40, 1.2, 3.76], 2.48)])

def test_calcular_media(notas, esperado):
    assert calcular_media(notas) == pytest.approx(esperado)