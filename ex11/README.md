# Atividade 11 — Pipeline de CI com GitHub Actions

Calculadora simples com pipeline de integração contínua exigindo lint, testes e cobertura mínima de 80%.

## Estrutura

```
ex11/
├── calculadora.py
├── test_calculadora.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
pytest --cov=calculadora --cov-report=term-missing --cov-fail-under=80
flake8 calculadora.py test_calculadora.py
```
