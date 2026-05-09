# Atividade 11 — Pipeline de CI com GitHub Actions

![CI](https://github.com/SEU_USUARIO/teste_de_software/actions/workflows/ci.yml/badge.svg)

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
flake8 calculadora.py test_calculadora.py --max-line-length=100
```

## Histórico do pipeline

A progressão exigida pelo enunciado fica registrada no `git log`:

1. **vermelho** — `ex11: adiciona pipeline CI ...` (testes incompletos, cobertura ≈ 65%, falha em `--cov-fail-under=80`)
2. **testes adicionados** — `ex11: adiciona testes para dividir/0, potencia e raiz_quadrada`
3. **verde** — pipeline passa após cobertura > 80%
4. **badge** — este commit

