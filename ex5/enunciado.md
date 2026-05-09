# Atividade 05 — Teste de Mutação

## Objetivo

Comparar a eficácia de uma suíte de testes contra **mutantes inseridos manualmente** e **mutantes gerados automaticamente** pela ferramenta `mutmut`, identificando os pontos fortes e fracos de cada abordagem.

## Tarefas

1. **Criar um código simples** em Python — uma calculadora com algumas operações básicas (somar, subtrair, multiplicar, dividir, etc.) é suficiente.
2. **Implementar a suíte de testes** que cubra todas as operações.
3. **Inserir mutantes manualmente** em um arquivo separado, fazendo pequenas alterações no código original (trocar operadores, inverter condições, mudar constantes).
4. **Rodar os testes contra cada mutante** e registrar quem foi *morto* (teste falhou) ou *sobreviveu* (teste passou).
5. **Executar o `mutmut`** sobre o mesmo código e comparar o resultado com a análise manual.
6. **Escrever um relatório** comparando: quantidade de mutantes, tipos de mutação, score, esforço e valor de cada abordagem.

## Entregável

Estrutura sugerida do projeto:

```
ex5/
├── calculadora.py        # codigo sob teste
├── test_calculadora.py   # suite de testes
├── mutantes_manuais.py   # mutantes inseridos manualmente
├── test_mutantes.py      # script que avalia os mutantes manuais
├── relatorio.md          # comparacao manual vs mutmut
└── README.md
```

## Comandos esperados

```bash
# Suite original
python -m unittest test_calculadora -v

# Avaliacao dos mutantes manuais
python test_mutantes.py

# Mutacao automatizada
mutmut run
mutmut results
```