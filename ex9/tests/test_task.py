from datetime import datetime, timedelta

import pytest

from task_manager.task import Task, Priority, Status


@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


def test_estado_inicial(task_valida):
    task_valida.validar()
    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.status == Status.PENDENTE


def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()


def test_prazo_no_passado_invalido():
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.MEDIA, prazo)
    with pytest.raises(ValueError):
        task.validar()


def test_ciclo_vida_transicao_valida(task_valida):
    assert task_valida.status == Status.PENDENTE
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO
    task_valida.status = Status.CONCLUIDA
    assert task_valida.status == Status.CONCLUIDA


def test_status_default_pendente():
    prazo = datetime.now() + timedelta(days=1)
    t = Task(None, "X1Y2Z", "d", Priority.BAIXA, prazo)
    assert t.status == Status.PENDENTE
