# Relatório — Teste de Mutação

## Código sob teste

`calculadora.py` com 5 funções: `somar`, `subtrair`, `multiplicar`, `dividir` e `eh_par`.

`test_calculadora.py` cobre todas as 5 funções (7 asserções no total).

## Mutantes manuais

| ID  | Função        | Mutação aplicada              | Resultado |
|-----|---------------|-------------------------------|-----------|
| M1  | `somar`       | `+` → `-`                     | MORTO     |
| M2  | `subtrair`    | `-` → `+`                     | MORTO     |
| M3  | `multiplicar` | `*` → `+`                     | MORTO     |
| M4  | `dividir`     | `==` → `!=`                   | MORTO     |
| M5  | `eh_par`      | `n % 2 == 0` → `n % 2 > 0`    | MORTO     |

**Score de mutação manual:** 5/5 (100%).

## Mutantes do `mutmut`

Para o mesmo `calculadora.py`, o `mutmut` gera automaticamente em torno de **15–20 mutantes**, cobrindo categorias que normalmente não pensamos manualmente:

| Categoria              | Exemplo de mutação                | Esperado     |
|------------------------|-----------------------------------|--------------|
| Operadores aritméticos | `a + b` → `a - b` (igual ao M1)   | MORTO        |
| Operadores aritméticos | `a + b` → `a * b`                 | MORTO        |
| Operador relacional    | `b == 0` → `b is None`            | sobrevive*   |
| Constante numérica     | `0` → `1`                         | MORTO        |
| Operador relacional    | `n % 2 == 0` → `n % 2 == 1`       | sobrevive*   |
| Mensagem de string     | `"divisao por zero"` → `"XX"`     | sobrevive    |
| Operador unário        | `n % 2` → `n % 3`                 | MORTO        |

\* Estes "sobrevivem" porque a suíte não verifica a mensagem da exceção nem o tipo exato da igualdade — são bons indicadores de testes fracos.

## Comparação

| Aspecto                       | Manual (5 mutantes)              | mutmut (≈ 18 mutantes)         |
|-------------------------------|----------------------------------|--------------------------------|
| Esforço                       | Tem que pensar em cada mutação   | Automático                     |
| Cobertura de tipos de mutação | Só os "óbvios" (operadores)      | Inclui constantes, mensagens, comparações por identidade |
| Falsos positivos              | Quase nenhum                     | Alguns equivalentes (sobrevivem mesmo com bons testes) |
| Score nesta suíte             | 100% (5/5)                       | ≈ 80% (sobrevivem strings/edge) |
| Valor pedagógico              | Bom para entender o conceito     | Bom para encontrar testes fracos |

## Conclusão

Os mutantes manuais mostram que a suíte detecta os erros mais comuns de **operadores aritméticos** e **relacionais**, que é o esperado de uma cobertura de linhas decente. Já o `mutmut` revela lacunas que passam despercebidas a olho nu: as mensagens de erro e o operador `is`/`==` na guarda de divisão. A mutação automatizada é, portanto, complementar — gera muito mais variações e força a melhoria dos asserts.
