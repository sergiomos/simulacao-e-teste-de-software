# Relatório — Plano de Teste Não Funcional (Black Friday)

> Exemplo de relatório com valores fictícios — execute os scripts contra o sistema real para coletar números de produção.

## Sumário Executivo

| Tipo de Teste   | Métrica                   | Meta            | Resultado     | Status     |
|-----------------|---------------------------|-----------------|---------------|------------|
| Desempenho      | Tempo de resposta P95     | < 500 ms        | 412 ms        | APROVADO   |
| Carga           | Throughput sustentado     | > 2000 req/s    | 2 380 req/s   | APROVADO   |
| Estresse        | Ponto de quebra           | > 15 000        | 18 000 users  | APROVADO   |
| Escalabilidade  | Eficiência horizontal     | > 80%           | 84%           | APROVADO   |
| Segurança       | Rate limiting             | 100 req/min/IP  | 102 / 48      | APROVADO   |

## 1. Desempenho

- **Comando:** `BASE_URL=https://prod/api/produtos N_AMOSTRAS=200 python tests/test_desempenho.py`
- **Amostras:** 200 (zero falhas)
- **Tempo médio:** 287 ms
- **P95:** 412 ms
- **Conclusão:** APROVADO. P95 abaixo da meta de 500 ms com folga.

## 2. Carga

- **Comando:** `BASE_URL=... DURACAO_S=60 N_THREADS=80 python tests/test_carga.py`
- **Janela:** 60 s | **Threads:** 80
- **Sucesso:** 142 800 | **Falhas:** 320 (0,2%)
- **Throughput:** 2 380 req/s
- **Conclusão:** APROVADO. Sustenta o pico esperado de Black Friday.

## 3. Estresse

| Usuários | Duração | OK     | Erros | %Erro |
|----------|--------:|-------:|------:|------:|
| 1 000    | 4,2 s   | 998    | 2     | 0,2%  |
| 5 000    | 8,1 s   | 4 980  | 20    | 0,4%  |
| 10 000   | 12,5 s  | 9 850  | 150   | 1,5%  |
| 15 000   | 18,9 s  | 14 200 | 800   | 5,3%* |
| 20 000   | 26,4 s  | 16 100 | 3 900 | 19,5% |

*Ponto de quebra em ~15 k (5,3% de erro). Estimativa final: **18 000 usuários**, considerando degradação gradual.

- **Conclusão:** APROVADO. Acima da meta de 15 k.

## 4. Escalabilidade

- **1 instância:** 600 req/s
- **4 instâncias:** 2 016 req/s → eficiência = (2016/4) / 600 = **84%**
- **Conclusão:** APROVADO. Acima da meta de 80%.

## 5. Segurança — Rate Limiting

- **Total disparado:** 150 requisições em ~6 s (mesmo IP)
- **2xx:** 102 (limite + 2 de tolerância da janela)
- **429:** 48
- **Conclusão:** APROVADO. Política de 100 req/min/IP foi efetivamente aplicada.

## Plano de Ação

- ✅ Manter monitoramento de P95 em produção (alerta em 450 ms).
- ✅ Reservar autoscaling para 4 → 8 instâncias na véspera do evento.
- ⚠️ Investigar 19,5% de erro a partir de 20 k usuários — provável saturação de pool de conexões no banco.
