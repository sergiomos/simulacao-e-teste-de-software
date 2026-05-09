# Atividade - Sistema de Estoque

## Contexto

Implemente a classe `Estoque` usando **estritamente a metodologia TDD**. Para cada funcionalidade, escreva o teste **antes** do código de produção.

Evidencie as fases **RED**, **GREEN** e **REFACTOR** com comentários no código.

---

## Operações a implementar

1. `adicionar_produto(nome, quantidade)`: adiciona produto ao estoque;
2. `remover_produto(nome, quantidade)`: remove unidades de um produto;
3. `consultar_quantidade(nome)`: retorna a quantidade disponível;
4. `listar_produtos()`: retorna lista dos produtos com quantidade > 0;
5. `produto_mais_estocado()`: retorna nome do produto com maior quantidade.

---

## Regras de negócio

- Não é possível remover mais unidades do que o disponível;
- Adicionar um produto já existente **incrementa** a quantidade (não substitui);
- Não é permitido adicionar ou remover quantidade ≤ 0;
- `produto_mais_estocado()` retorna `None` se o estoque estiver vazio;
- Consultar produto inexistente retorna `0`.

---

## Entregável

- `estoque.py`: classe `Estoque`;
- `test_estoque.py`: suite de testes;
- Ao menos **10 testes** cobrindo casos normais e de erro;
- Todos os testes devem passar ao final.

---

## Critério TDD (obrigatório)

Cada método implementado deve ser precedido pelo(s) teste(s) correspondente(s). A sequência **RED → GREEN → REFACTOR** deve ser evidenciada em comentários.
