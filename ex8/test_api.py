import pytest
import requests
import jsonschema


BASE_URL = "https://jsonplaceholder.typicode.com"
AUTH_URL = "https://httpbin.org/basic-auth/user/passwd"
STATUS_URL = "https://httpbin.org/status/400"

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}


@pytest.fixture
def post_criado():
    """Cria um post via POST e tenta remover apos o teste (setup/teardown)."""
    payload = {"title": "Teste fixture", "body": "conteudo", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    post = resp.json()
    yield post
    # teardown: jsonplaceholder simula a remocao mas nao persiste
    requests.delete(f"{BASE_URL}/posts/{post['id']}")


def test_listar_posts_status_e_lista_nao_vazia():
    """1. GET /posts -> 200 e lista com elementos."""
    resp = requests.get(f"{BASE_URL}/posts")
    assert resp.status_code == 200
    dados = resp.json()
    assert isinstance(dados, list)
    assert len(dados) > 0


def test_schema_post_individual():
    """2. GET /posts/1 -> schema validado por jsonschema."""
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200
    jsonschema.validate(instance=resp.json(), schema=POST_SCHEMA)


def test_recurso_inexistente_retorna_404():
    """3. GET /posts/9999 -> 404."""
    resp = requests.get(f"{BASE_URL}/posts/9999")
    assert resp.status_code == 404


def test_criar_post_retorna_id():
    """4. POST /posts -> 201 com id no corpo da resposta."""
    payload = {"title": "novo post", "body": "conteudo", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert "id" in body
    assert body["title"] == "novo post"


def test_atualizar_post_alterando_titulo():
    """5. PUT /posts/1 -> 200 e titulo alterado."""
    payload = {"id": 1, "title": "titulo alterado", "body": "y", "userId": 1}
    resp = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert resp.status_code == 200
    assert resp.json()["title"] == "titulo alterado"


def test_deletar_post_status_2xx():
    """6. DELETE /posts/1 -> 200 ou 204."""
    resp = requests.delete(f"{BASE_URL}/posts/1")
    assert resp.status_code in (200, 204)


def test_dados_invalidos_retorna_4xx():
    """7. Endpoint que retorna 400 para validar a asserção de erro client-side."""
    resp = requests.get(STATUS_URL)
    assert 400 <= resp.status_code < 500


def test_endpoint_autenticado_sem_credencial():
    """8a. GET autenticado SEM credencial -> 401."""
    resp = requests.get(AUTH_URL)
    assert resp.status_code == 401


def test_endpoint_autenticado_com_credencial():
    """8b. GET autenticado COM credencial valida -> 200."""
    resp = requests.get(AUTH_URL, auth=("user", "passwd"))
    assert resp.status_code == 200


def test_criar_post_usando_fixture(post_criado):
    """9. Usa a fixture post_criado para validar o recurso criado no setup."""
    assert "id" in post_criado
    assert post_criado["title"] == "Teste fixture"


def test_tempo_resposta_menor_que_2s():
    """10. GET /posts/1 deve responder em menos de 2 segundos."""
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200
    assert resp.elapsed.total_seconds() < 2.0
