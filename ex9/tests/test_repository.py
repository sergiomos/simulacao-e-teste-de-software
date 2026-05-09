"""Testes de COMPONENTE do TaskRepository: logica interna real, dependencia
externa (storage) substituida por mock."""

from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository


@pytest.fixture
def mock_storage():
    return Mock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Desc", Priority.BAIXA, prazo)


# 1. Estado + interacao: save atribui id sequencial
def test_save_atribui_id(repo, task):
    resultado = repo.save(task)
    assert resultado.id == 1


def test_save_ids_sequenciais(repo):
    prazo = datetime.now() + timedelta(days=1)
    t1 = Task(None, "A", "d", Priority.BAIXA, prazo)
    t2 = Task(None, "B", "d", Priority.BAIXA, prazo)
    assert repo.save(t1).id == 1
    assert repo.save(t2).id == 2


# 2. Mock: save chama storage.add com argumentos corretos
def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)
    mock_storage.add.assert_called_once_with(1, task)


# 3. Stub: find_by_id delega ao storage.get
def test_find_by_id_usa_storage(repo, task, mock_storage):
    mock_storage.get.return_value = task
    resultado = repo.find_by_id(1)
    assert resultado is task
    mock_storage.get.assert_called_once_with(1)


# 4. Sequencia: save seguido de find_by_id - colaboracao
def test_save_seguido_find_by_id(repo, task, mock_storage):
    # configura o stub para devolver a task apos o save
    salva = repo.save(task)
    mock_storage.get.return_value = salva
    encontrada = repo.find_by_id(salva.id)
    assert encontrada is salva


# 5. Isolamento: find_all retorna lista vazia quando storage nao tem itens
def test_find_all_lista_vazia(repo, mock_storage):
    mock_storage.get_all.return_value = []
    assert repo.find_all() == []


def test_delete_delega_ao_storage(repo, mock_storage):
    mock_storage.delete.return_value = True
    assert repo.delete(1) is True
    mock_storage.delete.assert_called_once_with(1)
