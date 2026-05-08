# Atividade 06 — Calculadora com Repositório de Histórico

Sistema de calculadora com persistência de histórico, exercitando testes de unidade, integração e *test doubles* (stubs e mocks).

## Estrutura

```
ex6/
├── src/
│   ├── calculadora.py     # logica de calculo
│   └── repositorio.py     # persistencia em memoria
├── tests/
│   ├── test_unidade.py    # Parte 1 - testes unitarios com stub
│   ├── test_integracao.py # Parte 2 - integracao com repositorio real
│   └── test_doubles.py    # Parte 3 - stub vs mock + bug
├── requirements.txt
├── README.md
└── relatorio.md
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução dos testes

```bash
python -m unittest discover tests -v
```

## Cobertura

```bash
coverage run --source=src -m unittest discover tests
coverage report -m
coverage html
```
