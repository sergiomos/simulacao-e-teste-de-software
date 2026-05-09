# Atividade - Suíte de Testes para uma API REST

## Objetivo

Construir uma suíte de testes automatizados para uma API REST pública, aplicando os conceitos de teste de sistema vistos nesta aula: status codes, schema, validação, autenticação, CRUD e fixtures.

## Entrega

Repositório público no GitHub:
- `test_api.py`
- `README.md`

### Ferramentas obrigatórias

- `requests` + `pytest`
- `jsonschema`

### APIs sugeridas (livre escolha)

- https://reqres.in
- https://jsonplaceholder.typicode.com
- https://pokeapi.co
- https://the-dog-api.com
- Qualquer API pública documentada

> ⚠️ **Atenção:** a API escolhida deve ter ao menos um endpoint autenticado **ou** um endpoint de criação de recurso.

---

## Requisitos da Suíte de Testes

A suíte deve conter no mínimo os seguintes testes:

| #  | Teste                                                       | Tipo          |
|----|-------------------------------------------------------------|---------------|
| 1  | GET em coleção → status 200, lista não vazia                | Status code   |
| 2  | GET em recurso existente → validar schema com `jsonschema`  | Schema        |
| 3  | GET em recurso inexistente → status 404                     | Caso negativo |
| 4  | POST criando recurso → status 201, id no retorno            | CREATE        |
| 5  | PUT ou PATCH atualizando recurso → campo alterado           | UPDATE        |
| 6  | DELETE → status 200 ou 204                                  | DELETE        |
| 7  | Envio de dados inválidos → status 4xx                       | Validação     |
| 8  | Endpoint autenticado: com e sem credencial                  | Autenticação  |
| 9  | Usar `@pytest.fixture` em pelo menos 1 teste                | Fixture       |
| 10 | Asserção de tempo de resposta < 2,0 s                       | Performance   |

---

## Estrutura do Repositório

Estrutura mínima esperada no GitHub:

```
meu-projeto/
├── test_api.py         # suíte de testes (pytest)
├── requirements.txt    # dependências (requests, pytest, jsonschema)
└── README.md           # documentação do projeto
```

O `README.md` deve conter:

1. Nome da API escolhida e link para sua documentação
2. Justificativa da escolha
3. Instruções de instalação (`pip install -r requirements.txt`)
4. Instrução de execução (`pytest -v`)
5. Descrição dos testes implementados

### Restrições

- Não usar ferramentas gráficas (Postman, Insomnia) — apenas código Python
- Não usar `time.sleep()` sem justificativa no comentário
- Cada função de teste deve ter **docstring** explicando o que valida

---

## Configuração do Projeto

### Arquivo `requirements.txt`

```
requests
pytest
jsonschema
```

### Instalação e execução

```bash
# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar todos os testes com saída detalhada
pytest test_api.py -v

# Executar e salvar relatório
pytest test_api.py -v > resultado.txt
```

---

## Esqueleto Sugerido — `test_api.py` (parte 1)

```python
import requests
import pytest
import jsonschema

# URL base da API escolhida pelo grupo
BASE_URL = "https://sua-api-aqui.com"

# Schema mínimo esperado para o recurso principal
SCHEMA_RECURSO = {
    "type": "object",
    "required": ["id"],  # adaptar aos campos reais
    "properties": {
        "id": {"type": "integer"},
        # adicionar os demais campos obrigatórios da API
    }
}

@pytest.fixture
def recurso_criado():
    """Cria um recurso antes do teste e remove após (setup/teardown)."""
    payload = {"nome": "Teste", "campo": "valor"}  # adaptar
    resp = requests.post(f"{BASE_URL}/recurso", json=payload)
    assert resp.status_code == 201
    recurso = resp.json()
    yield recurso
    # teardown: remover o recurso criado
    requests.delete(f"{BASE_URL}/recurso/{recurso['id']}")
```

## Esqueleto Sugerido — `test_api.py` (parte 2)

```python
def test_listar_recursos():
    """GET /recursos -> 200 e lista não vazia."""
    resp = requests.get(f"{BASE_URL}/recursos")
    assert resp.status_code == 200
    assert len(resp.json()) > 0

def test_schema_recurso():
    """GET /recursos/1 -> schema válido."""
    resp = requests.get(f"{BASE_URL}/recursos/1")
    assert resp.status_code == 200
    jsonschema.validate(instance=resp.json(), schema=SCHEMA_RECURSO)

def test_recurso_inexistente():
    """GET /recursos/9999 -> 404."""
    resp = requests.get(f"{BASE_URL}/recursos/9999")
    assert resp.status_code == 404

def test_tempo_resposta():
    """GET deve responder em menos de 2 segundos."""
    resp = requests.get(f"{BASE_URL}/recursos/1")
    assert resp.elapsed.total_seconds() < 2.0

def test_criar_com_fixture(recurso_criado):
    """Usa fixture: verifica recurso criado no setup."""
    assert "id" in recurso_criado
```
