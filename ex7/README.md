# Atividade — Sistema de Estoque (TDD)

Classe `Estoque` desenvolvida estritamente por TDD: cada método foi precedido por seus testes, evidenciando o ciclo **RED → GREEN → REFACTOR**.

## Estrutura

```
ex7/
├── estoque.py       # classe Estoque
├── test_estoque.py  # 13 testes
└── README.md
```

## Execução

```bash
python -m unittest test_estoque -v
```

## Histórico TDD

O `git log` reflete os ciclos:

- `RED — primeiro teste de adicionar_produto`
- `GREEN — implementa Estoque minimo`
- `RED — testes para incremento e validacao`
- `GREEN — validacao e incremento`
- `RED — testes de remover, listar, mais_estocado`
- `GREEN — implementa remover, listar, consultar, produto_mais_estocado`
- `REFACTOR — extrai helper de validacao`

## Cobertura dos requisitos

| # | Operação                     | Testes que cobrem                                               |
|---|------------------------------|-----------------------------------------------------------------|
| 1 | `adicionar_produto`          | novo, existente (incrementa), zero inválido, negativo inválido  |
| 2 | `remover_produto`            | normal, maior que disponível, inexistente, quantidade ≤ 0       |
| 3 | `consultar_quantidade`       | inexistente retorna 0 (+ implícito em todos os outros testes)   |
| 4 | `listar_produtos`            | só com `> 0`, vazio                                             |
| 5 | `produto_mais_estocado`      | retorna nome, retorna `None` quando vazio                       |
