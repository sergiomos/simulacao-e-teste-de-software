# Atividade 09 — Sistema Task Manager

Sistema de gerenciamento de tarefas em Python com testes orientados a objetos e componentes (Aula 09).

## Estrutura

```
ex9/
├── task_manager/
│   ├── __init__.py
│   ├── task.py          # Task + enums Priority/Status
│   ├── storage.py       # InMemoryStorage
│   ├── repository.py    # TaskRepository
│   └── service.py       # TaskService (bonus)
├── tests/
│   ├── __init__.py
│   ├── test_task.py        # testes UNITARIOS (sem mocks)
│   └── test_repository.py  # testes de COMPONENTE (storage mockado)
├── requirements.txt
└── README.md
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução dos testes

```bash
pytest -v
```

Com cobertura (opcional):

```bash
pytest --cov=task_manager
```

## Testes implementados

`test_task.py` (6 testes — unitários, sem mocks):

- `test_estado_inicial` — todos os atributos atribuídos, status default `PENDENTE`
- `test_titulo_curto_invalido` — `validar()` lança `ValueError`
- `test_prazo_no_passado_invalido` — `validar()` lança `ValueError`
- `test_ciclo_vida_transicao_valida` — `PENDENTE → EM_PROGRESSO → CONCLUIDA`
- `test_ciclo_vida_transicao_invalida` — atribuir status fora do enum → `ValueError`
- `test_status_default_pendente` — criação sem status explícito

`test_repository.py` (6 testes — componente, com `Mock`):

- `test_save_atribui_id` — estado: `task.id` definido após `save()`
- `test_save_ids_sequenciais` — IDs incrementais
- `test_save_chama_storage_add` — mock com `assert_called_once_with`
- `test_find_by_id_usa_storage` — stub com `return_value`
- `test_save_seguido_find_by_id` — colaboração entre métodos
- `test_find_all_lista_vazia` — isolamento via stub
- `test_delete_delega_ao_storage` — mock de delegação
