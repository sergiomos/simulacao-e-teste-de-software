# Atividade — Plano de Teste Não Funcional (E-commerce Black Friday)

## Cenário

Desenvolva um plano de teste completo para um sistema de e-commerce que será lançado na Black Friday, incorporando uma métrica de cada tipo de teste não funcional.

## Requisitos do Sistema

- 10.000 usuários simultâneos esperados na Black Friday
- Tempo de resposta < 500ms para 95% das requisições
- Disponibilidade de 99.9% durante o evento
- Proteção contra ataques e vazamento de dados

## Métricas por Tipo de Teste

| Tipo de Teste   | Métrica Obrigatória      | Meta Definida       |
|-----------------|--------------------------|---------------------|
| Desempenho      | Tempo de resposta P95    | < 500 ms            |
| Carga           | Throughput sustentado    | > 2000 req/s        |
| Estresse        | Ponto de quebra          | > 15.000 usuários   |
| Escalabilidade  | Eficiência horizontal    | > 80%               |
| Segurança       | Rate limiting            | 100 req/min/IP      |

## Entregável

Exemplos de testes implementados em **Python** para cada tipo, incluindo:

- Código funcional
- Métricas coletadas
- Relatório de resultados com análise de **aprovação/reprovação** das metas
