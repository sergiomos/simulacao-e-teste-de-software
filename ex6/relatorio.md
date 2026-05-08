# Relatório — Atividade 06

## Resultados dos testes

```
Ran 44 tests in 0.005s
OK
```

Distribuição:

- `test_unidade.py`: 28 testes (entrada/saída, tipagem, limites, exceções, mensagens, fluxos de controle)
- `test_integracao.py`: 5 testes (operações sequenciais, formato do histórico, ordem, exceções não gravam)
- `test_doubles.py`: 11 testes (3 com stub, 7 com mock, 1 que detecta o bug em `potencia`)

## Bug encontrado e correção

### Localização

Arquivo `src/calculadora.py`, método `potencia`.

### Comportamento incorreto

A string registrada no histórico usava o operador `*` ao invés de `**`:

```python
# antes
self.repositorio.salvar(f"{base} * {expoente} = {resultado}")
```

Isso produzia entradas inconsistentes do tipo `2 * 3 = 8` (que é matematicamente errado — `2 * 3 = 6`).

### Como o bug foi detectado

O teste `TestBugPotencia.test_mock_revela_bug_em_potencia` usa um mock para verificar o argumento exato passado ao repositório:

```python
self.calc.potencia(2, 3)
self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")
```

Saída do `assert_called_once_with` antes da correção:

```
AssertionError: expected call not found.
Expected: salvar('2 ** 3 = 8')
  Actual: salvar('2 * 3 = 8')
```

### Correção aplicada

```python
# depois
self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")
```

## Reflexão — Stub vs Mock

| Aspecto                   | Stub                                        | Mock                                                   |
|---------------------------|---------------------------------------------|--------------------------------------------------------|
| Foco                      | Estado: fornecer valor pré-definido         | Comportamento: verificar interação                     |
| Verificação               | Não verifica chamadas                       | Verifica `quem`, `quantas vezes`, `com quais args`     |
| Quando usar               | Não dá pra usar a dependência real          | Quero garantir contrato de chamada com a dependência   |
| Exemplo nesta atividade   | `stub_repo.total.return_value = 0`          | `mock_repo.salvar.assert_called_once_with("4 + 6 = 10")` |

Na prática, o **stub** isola a calculadora do repositório para testar lógica pura (resultados de cálculo). O **mock** verifica a colaboração entre os módulos — sem ele, o bug em `potencia` passaria despercebido pelos testes de unidade tradicionais (que olham apenas o retorno).

## Cobertura

A medição com `coverage.py` não foi executada neste ambiente por restrição de rede no índice PyPI. A inspeção manual do código indica:

- `repositorio.py`: 100% — todos os métodos exercitados por `test_integracao.py`
- `calculadora.py`: 100% — cada ramo `if` (validação de tipo, divisão por zero) coberto por `TestForaDoIntervalo`, `TestTipagem` e `TestFluxosDeControle`

Para reproduzir localmente:

```bash
pip install coverage
coverage run --source=src -m unittest discover tests
coverage report -m
```
