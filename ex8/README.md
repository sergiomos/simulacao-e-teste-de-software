# Atividade — Suíte de Testes para uma API REST

Suíte de testes automatizados em `pytest` exercitando os principais conceitos de teste de sistema: status codes, schema, validação, autenticação, CRUD, fixtures e performance.

## API escolhida

- **Principal:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) — API REST pública e estável, com endpoints para CRUD de posts, comentários, álbuns, usuários etc.
- **Autenticação:** [httpbin.org/basic-auth](https://httpbin.org) — fornece um endpoint que exige Basic Auth, ideal para o caso de uso "com e sem credencial".
- **Status code 4xx:** `httpbin.org/status/400` — para demonstrar a asserção de erro client-side.

### Justificativa

JSONPlaceholder é a referência canônica para exercícios de teste de API: documentação simples, sempre disponível, suporta todos os verbos HTTP exigidos no enunciado e simula 201/200/404. Como não exige autenticação, complementamos com `httpbin.org/basic-auth` para cobrir o requisito de endpoint autenticado.

## Estrutura

```
ex8/
├── test_api.py
├── requirements.txt
└── README.md
```

## Instalação

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Execução

```bash
pytest test_api.py -v
```

Para gravar o relatório:

```bash
pytest test_api.py -v > resultado.txt
```

## Testes implementados

| #  | Função                                            | Tipo          |
|----|---------------------------------------------------|---------------|
| 1  | `test_listar_posts_status_e_lista_nao_vazia`      | Status code   |
| 2  | `test_schema_post_individual`                     | Schema        |
| 3  | `test_recurso_inexistente_retorna_404`            | Caso negativo |
| 4  | `test_criar_post_retorna_id`                      | CREATE        |
| 5  | `test_atualizar_post_alterando_titulo`            | UPDATE        |
| 6  | `test_deletar_post_status_2xx`                    | DELETE        |
| 7  | `test_dados_invalidos_retorna_4xx`                | Validação     |
| 8a | `test_endpoint_autenticado_sem_credencial`        | Autenticação  |
| 8b | `test_endpoint_autenticado_com_credencial`        | Autenticação  |
| 9  | `test_criar_post_usando_fixture`                  | Fixture       |
| 10 | `test_tempo_resposta_menor_que_2s`                | Performance   |
