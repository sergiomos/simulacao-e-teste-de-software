import pytest
from ex2 import validar_cpf, formatar_cpf


@pytest.fixture
def cpfs_validos():
    return [
        "795.564.560-07",
        "935.892.260-56",
        "424.204.450-07",
    ]


@pytest.fixture
def cpfs_invalidos():
    return [
        "12345678901",
        "00000000000",
        "11111111111",
        "12345678900",
        "111",
        "123456789012",
        "123.456.789-ab",
        "",
        None,
    ]


def test_validar_cpf_valido_padrao(cpfs_validos):
    for cpf in cpfs_validos:
        resultado = validar_cpf(cpf)
        assert resultado is True


@pytest.mark.parametrize("cpf", ["795.564.560-07", "935.892.260-56", "424.204.450-07"])
def test_validar_cpf_valido_com_zeros(cpf):
    resultado = validar_cpf(cpf)
    assert resultado is True


def test_validar_cpf_invalido_digitos_verificadores_errados(cpfs_invalidos):
    resultado = validar_cpf(cpfs_invalidos[0])
    assert resultado is False


def test_validar_cpf_invalido_todos_digitos_iguais(cpfs_invalidos):
    resultado = validar_cpf(cpfs_invalidos[2])
    assert resultado is False


def test_validar_cpf_invalido_menos_de_11_digitos(cpfs_invalidos):
    resultado = validar_cpf(cpfs_invalidos[4])
    assert resultado is False


def test_validar_cpf_invalido_mais_de_11_digitos(cpfs_invalidos):
    resultado = validar_cpf(cpfs_invalidos[5])
    assert resultado is False


def test_validar_cpf_invalido_com_letras(cpfs_invalidos):
    resultado = validar_cpf(cpfs_invalidos[6])
    assert resultado is False


def test_formatar_cpf_valido(cpfs_validos):
    cpf = cpfs_validos[0]
    resultado = formatar_cpf(cpf)
    assert "." in resultado and "-" in resultado


def test_formatar_cpf_invalido_lanca_excecao(cpfs_invalidos):
    cpf = cpfs_invalidos[0]
    with pytest.raises(ValueError, match="CPF inválido"):
        formatar_cpf(cpf)


def test_validar_cpf_vazio_ou_none(cpfs_invalidos):
    resultado_vazio = validar_cpf(cpfs_invalidos[7])
    resultado_none = validar_cpf(cpfs_invalidos[8])
    assert resultado_vazio is False
    assert resultado_none is False
