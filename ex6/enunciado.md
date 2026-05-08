# CC8550 — Simulação e Teste de Software

**Atividade 06 — Testes de Unidade e Integração**
**Aplicação Prática:** Calculadora com Repositório de Histórico
*Prof. Luciano Rossi | Centro Universitário FEI | 13 de março de 2026*

## Objetivo da Atividade

Desenvolver e executar testes de unidade e integração para um sistema de calculadora com persistência de histórico. O objetivo é aplicar na prática os tipos de teste estudados em aula, incluindo o uso de *test doubles* (stubs e mocks) para testar componentes de forma isolada.

---

## 1. Descrição do Sistema

O sistema é composto por dois módulos que colaboram entre si:

- **Calculadora** — realiza as operações matemáticas e registra cada resultado via um repositório externo.
- **HistoricoRepositorio** — responsável por persistir e recuperar o histórico de operações (simularia um banco de dados ou arquivo).

> ⚠️ **Atenção:** O código abaixo contém um defeito intencional. Parte da atividade é descobri-lo por meio dos testes e documentar a correção aplicada.

### Módulo 1 — `src/repositorio.py`

```python
class HistoricoRepositorio:
    def __init__(self):
        self._registros = []

    def salvar(self, entrada: str) -> None:
        self._registros.append(entrada)

    def listar(self) -> list:
        return self._registros

    def limpar(self) -> None:
        self._registros.clear()

    def total(self) -> int:
        return len(self._registros)
```

### Módulo 2 — `src/calculadora.py`

```python
class Calculadora:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.resultado = 0

    def somar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a + b
        self.repositorio.salvar(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a - b
        self.repositorio.salvar(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a * b
        self.repositorio.salvar(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self.repositorio.salvar(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = base ** expoente
        # BUG: registro usa operador errado na string de historico
        self.repositorio.salvar(f"{base} * {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def obter_ultimo_resultado(self):
        return self.resultado
```

---

## 2. Parte 1 — Testes de Unidade

Os testes de unidade devem testar cada método da `Calculadora` de forma isolada, sem depender da implementação real do `HistoricoRepositorio`. Use um *stub* para substituir o repositório onde necessário.

### 2.1 Testes de Entrada e Saída

**Objetivo:** Validar se os parâmetros são interpretados corretamente e os valores retornados estão corretos.

**Exemplo fornecido:**

```python
from unittest.mock import MagicMock
import unittest

class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()  # stub do repositorio
        self.calc = Calculadora(self.repo)

    def test_soma_retorna_valor_correto(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)
```

> Implemente testes equivalentes para `subtrair`, `multiplicar`, `dividir` e `potencia`, cobrindo ao menos dois casos cada.

### 2.2 Testes de Tipagem

**Objetivo:** Confirmar que tipos incorretos são rejeitados com a exceção adequada.

**Exemplo fornecido:**

```python
def test_tipagem_string_rejeitada(self):
    with self.assertRaises(TypeError):
        self.calc.somar("5", 3)

def test_tipagem_none_rejeitado(self):
    with self.assertRaises(TypeError):
        self.calc.dividir(10, None)
```

> Implemente testes de tipagem para todas as operações matemáticas. Inclua ao menos um caso com `bool` — observe que em Python `bool` é subclasse de `int`. O comportamento é esperado?

### 2.3 Testes de Limite Inferior e Superior

**Objetivo:** Verificar o comportamento nas fronteiras do domínio numérico.

**Exemplo fornecido:**

```python
def test_limite_zero(self):
    self.assertEqual(self.calc.somar(0, 5), 5)

def test_limite_float_pequeno(self):
    self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

def test_limite_float_grande(self):
    import sys
    grande = sys.float_info.max / 2
    resultado = self.calc.somar(grande, grande)
    self.assertFalse(resultado == float('inf'))  # nao deve transbordar
```

> Implemente testes de limite para `dividir` (divisor muito pequeno, próximo de zero) e para `potencia` (expoente negativo, expoente fracionário).

### 2.4 Testes de Valores Fora do Intervalo

**Exemplo fornecido:**

```python
def test_divisao_por_zero_levanta_excecao(self):
    with self.assertRaises(ValueError):
        self.calc.dividir(10, 0)
```

### 2.5 Testes de Mensagens de Erro

**Objetivo:** Verificar se as mensagens de erro são claras e correspondem ao contrato da interface.

> ⚠️ **Atenção:** Evite usar `try/except` manual nos testes — se a exceção não for lançada, o teste passará silenciosamente sem nenhum assert. Use `assertRaisesRegex` para verificar a mensagem com segurança.

**Exemplo fornecido:**

```python
def test_mensagem_divisao_por_zero(self):
    with self.assertRaisesRegex(ValueError, "Divisao por zero"):
        self.calc.dividir(5, 0)

def test_mensagem_tipo_invalido(self):
    with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
        self.calc.somar("x", 1)
```

### 2.6 Testes de Fluxos de Controle

**Objetivo:** Exercitar todos os caminhos do código — cada `if` deve ser coberto com pelo menos um teste para cada ramo.

**Exemplo fornecido:**

```python
def test_caminho_divisao_normal(self):
    self.assertEqual(self.calc.dividir(10, 2), 5.0)

def test_caminho_divisao_erro(self):
    with self.assertRaises(ValueError):
        self.calc.dividir(10, 0)
```

> Use `coverage.py` para medir a cobertura após implementar todos os testes de unidade. O objetivo é atingir **100% de cobertura de linhas** em `calculadora.py`. Documente quais linhas ficaram descobertas (se houver) e por quê.

---

## 3. Parte 2 — Testes de Integração com Repositório Real

Nesta seção os dois módulos são testados juntos, usando a implementação real do `HistoricoRepositorio` (sem stubs). O objetivo é verificar a comunicação entre os componentes.

### 3.1 Operações Sequenciais

**Objetivo:** Verificar se múltiplas operações encadeadas produzem o estado correto.

**Exemplo fornecido:**

```python
class TestIntegracao(unittest.TestCase):
    def setUp(self):
        self.repo = HistoricoRepositorio()
        self.calc = Calculadora(self.repo)

    def test_operacoes_sequenciais(self):
        # 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        self.calc.somar(2, 3)
        self.calc.multiplicar(self.calc.obter_ultimo_resultado(), 4)
        self.calc.dividir(self.calc.obter_ultimo_resultado(), 2)

        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)
        self.assertEqual(self.repo.total(), 3)
```

### 3.2 Consistência do Histórico

**Exemplo fornecido:**

```python
def test_historico_registra_formato_correto(self):
    self.calc.somar(2, 3)
    self.calc.multiplicar(4, 5)
    registros = self.repo.listar()
    self.assertIn("2 + 3 = 5", registros)
    self.assertIn("4 * 5 = 20", registros)

def test_limpar_historico(self):
    self.calc.somar(1, 1)
    self.repo.limpar()
    self.assertEqual(self.repo.total(), 0)
```

---

## 4. Parte 3 — Test Doubles: Stub e Mock

Esta seção explora o uso de *test doubles* para testar a `Calculadora` em completo isolamento do `HistoricoRepositorio`.

### 4.1 Stub — controlando o estado do repositório

**Objetivo:** Testar a `Calculadora` sem depender da implementação real do repositório. O stub retorna valores pré-definidos, permitindo testar a lógica da calculadora independentemente.

**Exemplo fornecido:**

```python
from unittest.mock import MagicMock

class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        # stub: salvar() nao faz nada de verdade
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        # A calculadora pode ser testada mesmo antes do repositorio existir
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)
```

### 4.2 Mock — verificando o comportamento (interação)

**Objetivo:** Verificar se e como a `Calculadora` chama o repositório — não apenas o resultado retornado, mas a interação entre os componentes.

**Exemplo fornecido:**

```python
class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        # Verifica que salvar() foi chamado exatamente uma vez
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto(self):
        self.calc.somar(4, 6)
        # Verifica o argumento exato passado ao repositorio
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        # Se houve excecao, o repositorio NAO deve ter sido acionado
        self.mock_repo.salvar.assert_not_called()
```

> 1. Implemente um teste mock que verifique o argumento passado a `salvar()` para todas as operações.
> 2. Use o mock para detectar o bug intencional em `potencia` — qual string é registrada incorretamente?
> 3. Após identificar o bug, corrija-o em `calculadora.py` e documente a correção no relatório.

---

## 5. Tarefas

1. **Complete os exemplos** — implemente os testes marcados como "Implemente" seguindo os padrões mostrados.
2. **Adicione testes extras** — para cada categoria, crie ao menos um teste adicional além dos fornecidos.
3. **Descubra e corrija o bug** — use os testes mock de `potencia` para localizar e corrigir o defeito intencional.
4. **Meça a cobertura** — use `coverage.py` e documente: linhas cobertas, linhas não cobertas e justificativa.
5. **Redija o relatório** em `relatorio.md` com: resultados dos testes, cobertura obtida, bug encontrado/corrigido, e reflexão sobre a diferença entre stub e mock na prática.

### Estrutura do repositório

```
projeto_calculadora/
├── src/
│   ├── calculadora.py        # com bug corrigido
│   └── repositorio.py
├── tests/
│   ├── __init__.py
│   ├── test_unidade.py       # Parte 1
│   ├── test_integracao.py    # Parte 2
│   └── test_doubles.py       # Parte 3 (stub e mock)
├── requirements.txt
├── README.md
└── relatorio.md
```

### Comandos úteis

```bash
# Instalar dependencias
pip install -r requirements.txt

# Executar todos os testes
python -m unittest discover tests -v

# Medir cobertura
coverage run -m unittest discover tests
coverage report -m
coverage html  # gera relatorio em htmlcov/index.html
```
