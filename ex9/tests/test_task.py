"""Testes UNITARIOS da classe Task: sem dependencias externas, foco em
estado e ciclo de vida."""

from datetime import datetime, timedelta

import pytest

from task_manager.task import Task, Priority, Status


@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


# 1. Estado inicial - todos os atributos atribuidos e status default = PENDENTE
def test_estado_inicial(task_valida):
    task_valida.validar()
    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.status == Status.PENDENTE


# 2. Titulo invalido lanca ValueError
def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()


# 3. Prazo no passado lanca ValueError
def test_prazo_no_passado_invalido():
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.MEDIA, prazo)
    with pytest.raises(ValueError):
        task.validar()


# 4. Ciclo de vida - transicao PENDENTE -> EM_PROGRESSO
def test_ciclo_vida_transicao_valida(task_valida):
    assert task_valida.status == Status.PENDENTE
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO
    task_valida.status = Status.CONCLUIDA
    assert task_valida.status == Status.CONCLUIDA


# 5. Ciclo de vida - status fora do enum lanca ValueError
def test_ciclo_vida_transicao_invalida(task_valida):
    with pytest.raises(ValueError):
        task_valida.status = "concluida"  # string, nao Status


# Extra: estado padrao ao criar sem status explicito
def test_status_default_pendente():
    prazo = datetime.now() + timedelta(days=1)
    t = Task(None, "X1Y2Z", "d", Priority.BAIXA, prazo)
    assert t.status == Status.PENDENTE
