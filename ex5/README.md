# Atividade 05 — Teste de Mutação

Comparação entre **mutantes manuais** (5 inseridos à mão em uma calculadora simples) e **mutantes gerados automaticamente** pelo `mutmut`.

## Estrutura

```
ex5/
├── calculadora.py        # codigo sob teste
├── test_calculadora.py   # suite de testes
├── mutantes_manuais.py   # 5 mutantes inseridos manualmente
├── test_mutantes.py      # roda as asserções contra os mutantes
├── relatorio.md          # comparacao manual vs mutmut
└── README.md
```

## Execução

### Suite de testes

```bash
python -m unittest test_calculadora -v
```

### Mutação manual

```bash
python test_mutantes.py
```

Saída obtida:

```
Mutante                          | Status
--------------------------------------------------
M1: somar (+ -> -)               | MORTO
M2: subtrair (- -> +)            | MORTO
M3: multiplicar (* -> +)         | MORTO
M4: dividir (== -> !=)           | MORTO
M5: eh_par (== -> >)             | MORTO

Score de mutacao: 5/5 (100.0%)
```

### Mutação com mutmut

```bash
pip install mutmut
mutmut run --paths-to-mutate=calculadora.py
mutmut results
mutmut show all
```

## Resultados

Veja `relatorio.md`.
