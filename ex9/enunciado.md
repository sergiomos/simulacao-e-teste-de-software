# CC8550 — Simulação e Teste de Software

**Atividade 09 — Sistema Task Manager**
*Testes orientados a objetos e componentes*

## Objetivo

Desenvolver um Sistema de Gerenciamento de Tarefas simples em Python e escrever testes automatizados que exercitem, de forma explícita, os conceitos discutidos na Aula 09:

- **Testes de estado:** verificar que os atributos do objeto mudam corretamente após chamadas de método (não apenas o valor de retorno).
- **Setup e teardown:** usar fixtures do pytest para criar objetos em estado inicial válido antes de cada teste.
- **Isolamento de dependências com stubs e mocks:** substituir colaboradores reais por dublês de teste; usar **stubs** quando só é necessário fornecer uma resposta fixa, e **mocks** quando é preciso verificar se e como um método foi chamado.
- **Testes de interação entre métodos:** validar sequências de operações que dependem de chamadas anteriores (ex.: salvar antes de buscar).
- **Ciclo de vida do objeto:** verificar transições de estado válidas e comportamentos inválidos em cada fase.
- **Distinção entre teste unitário e de componente:** os testes de `Task` são testes unitários (classe isolada, sem dependências); os testes de `TaskRepository` são testes de componente (dependência externa `InMemoryStorage` mockada, colaboração interna real).

## O que o sistema faz?

- Criar tarefas com título, descrição, prioridade e prazo
- Listar todas as tarefas
- Buscar tarefa por ID
- Atualizar status da tarefa
- Deletar tarefas

---

## Estrutura do Projeto

```
task_manager/
├── task.py
├── storage.py
├── repository.py
├── service.py            # Bônus
tests/
├── test_task.py
├── test_repository.py
requirements.txt
README.md
```

### Tecnologias

- Python 3.8+
- `pytest`
- `pytest-mock`

---

## 1. Arquivo `task.py`

### O que implementar

#### 1. Enum `Priority`

```python
from enum import IntEnum

class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
```

#### 2. Enum `Status`

```python
from enum import Enum

class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"
```

#### 3. Classe `Task`

**Atributos:**

- `id: int` ou `None`
- `titulo: str`
- `descricao: str`
- `prioridade: Priority`
- `prazo: datetime`
- `status: Status` (padrão: `PENDENTE`)

**Métodos obrigatórios:**

- `validar()`: Verifica se título tem 3+ caracteres e prazo não é passado. Lança `ValueError` se inválido.

### Testes (`test_task.py`)

Estes são **testes unitários** da classe `Task`: ela não possui dependências externas, então nenhum mock é necessário. O foco está em verificar **estado** (atributos após criação) e **ciclo de vida** (transições de status válidas/inválidas).

Criar **pelo menos 5 testes**, cobrindo:

1. **Estado inicial:** após criação válida, verificar que todos os atributos foram atribuídos corretamente e que o status padrão é `PENDENTE` (teste de estado).
2. **Título inválido:** deve lançar `ValueError` (validação de contrato).
3. **Prazo no passado:** deve lançar `ValueError`.
4. **Ciclo de vida – transição válida:** alterar o status de `PENDENTE` para `EM_PROGRESSO` e verificar o novo estado do objeto.
5. **Ciclo de vida – transição inválida:** tentar definir um status com um valor fora do enum deve lançar `ValueError`.

Use uma fixture para evitar repetição na criação do objeto de teste:

```python
import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)

def test_estado_inicial(task_valida):
    task_valida.validar()  # nao deve lancar erro
    assert task_valida.titulo == "Estudar"
    assert task_valida.status == Status.PENDENTE  # estado padrao

def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()

def test_ciclo_vida_transicao(task_valida):
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO  # estado mudou
```

---

## 2. Arquivo `storage.py`

### Classe `InMemoryStorage`

Armazena dados em memória (dicionário).

**Atributo:**

- `_data`: `dict` vazio no `__init__`

**Métodos obrigatórios:**

- `add(id, item)`: Adiciona item com chave `id`
- `get(id)`: Retorna item ou `None`
- `get_all()`: Retorna lista com todos os valores
- `delete(id)`: Remove item, retorna `True`/`False`
- `clear()`: Limpa tudo

**Exemplo:**

```python
class InMemoryStorage:
    def __init__(self):
        self._data = {}

    def add(self, id, item):
        self._data[id] = item

    def get(self, id):
        return self._data.get(id)

    # ... outros metodos
```

---

## 3. Arquivo `repository.py`

### Classe `TaskRepository`

Gerencia persistência de tarefas.

**Atributos:**

- `storage`: `InMemoryStorage` (recebe no construtor)
- `_next_id`: `int` (começa em 1)

**Métodos obrigatórios:**

- `save(task)`: Atribui ID, salva no storage, retorna task
- `find_by_id(id)`: Busca e retorna task ou `None`
- `find_all()`: Retorna lista de todas as tasks
- `delete(id)`: Remove task

**Exemplo do método `save`:**

```python
def save(self, task):
    task.id = self._next_id
    self._next_id += 1
    self.storage.add(task.id, task)
    return task
```

### Testes (`test_repository.py`)

Estes são **testes de componente:** o `TaskRepository` é testado com sua lógica interna real, mas a dependência externa (`InMemoryStorage`) é substituída por um mock. Use fixtures para criar o repositório e a tarefa de teste.

#### Diferença entre stub e mock nesta atividade

- Use **stub** (valor de retorno configurado, sem verificação de chamada) quando só precisa que `storage.get()` retorne algo.
- Use **mock com assert** quando precisa verificar que `storage.add()` foi chamado com os argumentos corretos.

Criar **pelo menos 5 testes:**

1. **Interação – `save` atribui ID:** após `save()`, verificar que `task.id` foi definido (teste de estado + interação entre métodos).
2. **Mock – `save` chama `storage.add`:** verificar que o método `storage.add` foi chamado exatamente uma vez (mock com `assert_called_once()`).
3. **Stub – `find_by_id` delega ao storage:** configurar `mock_storage.get.return_value` e verificar que o repositório retorna o objeto correto.
4. **Sequência – `save` seguido de `find_by_id`:** verificar colaboração entre métodos (salvar e depois recuperar).
5. **Isolamento – `find_all` retorna lista vazia:** quando o storage não tem itens, `find_all()` deve retornar lista vazia.

**Exemplo com mock e stub:**

```python
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
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

# Teste de ESTADO: verifica que o atributo id mudou
def test_save_atribui_id(repo, task):
    resultado = repo.save(task)
    assert resultado.id == 1  # estado mudou

# Teste de MOCK: verifica como a dependencia foi usada
def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)
    mock_storage.add.assert_called_once_with(1, task)

# Teste de STUB: configura retorno e verifica delegacao
def test_find_by_id_usa_storage(repo, task, mock_storage):
    mock_storage.get.return_value = task  # stub
    resultado = repo.find_by_id(1)
    assert resultado == task
```

---

## 4. Arquivo `service.py` (BÔNUS)

### Classe `TaskService`

**Atributo:**

- `repository`: `TaskRepository` (recebe no construtor)

**Métodos:**

- `criar_tarefa(...)`: Cria, valida e salva
- `listar_todas()`: Retorna todas
- `atualizar_status(id, status)`: Atualiza status

---

## 5. Arquivos de Configuração

### `requirements.txt`

```
pytest==7.4.0
pytest-mock==3.11.1
```

### `README.md`

Incluir:

- Título e descrição
- Como instalar: `pip install -r requirements.txt`
- Como testar: `pytest -v`
- Estrutura do projeto

---

## 6. Checklist

### Implementação

- [ ] `Task` com enums `Priority` e `Status`
- [ ] Método `validar()` funcionando
- [ ] `InMemoryStorage` com 5 métodos
- [ ] `TaskRepository` com 4 métodos
- [ ] (Bônus) `TaskService`

### Testes alinhados à Aula 09

- [ ] Fixture para criação de objeto (setup)
- [ ] Teste de estado inicial (`status == PENDENTE`)
- [ ] Teste de ciclo de vida (transição de status)
- [ ] Testes de validação com `pytest.raises`
- [ ] Mock com `assert_called_once()` (verifica interação)
- [ ] Stub com `return_value` (isola dependência)
- [ ] Pelo menos 5 testes em `test_task.py`
- [ ] Pelo menos 5 testes em `test_repository.py`

### Configuração

- [ ] `README.md` completo

---

## 7. Dicas

1. Implemente e teste **uma classe por vez** — não avance antes de os testes da classe atual passarem.
2. `test_task.py` é teste **unitário**: sem mocks, foco em estado e ciclo de vida.
3. `test_repository.py` é teste **de componente**: mock apenas o storage (dependência externa); a lógica interna do repositório é real.
4. Prefira **mock com `assert_called_*`** quando o comportamento importante é *se* e *como* um colaborador foi chamado. Use **stub** (`return_value`) quando apenas precisa de um retorno fixo.
5. Use `pytest -v` para ver o nome de cada teste e identificar quais falham.

---

## 8. Como Executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar testes:

```bash
pytest -v
```

Executar com cobertura (opcional):

```bash
pytest --cov=task_manager
```

---

## 9. Exemplo de Uso

```python
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.storage import InMemoryStorage
from task_manager.repository import TaskRepository

# Criar componentes
storage = InMemoryStorage()
repo = TaskRepository(storage)

# Criar tarefa
prazo = datetime.now() + timedelta(days=5)
task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
task.validar()

# Salvar
task_salva = repo.save(task)
print(f"ID: {task_salva.id}")

# Buscar
encontrada = repo.find_by_id(1)
print(f"Titulo: {encontrada.titulo}")
```
