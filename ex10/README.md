# Atividade — Plano de Teste Não Funcional (E-commerce Black Friday)

Plano de teste não funcional cobrindo desempenho, carga, estresse, escalabilidade e segurança. Cada script Python coleta as métricas-alvo e imprime APROVADO/REPROVADO conforme as metas estabelecidas.

> Implementação **sem dependências externas**: usa apenas `urllib.request`, `threading`, `time` e `statistics` da biblioteca padrão.

## Metas

| Tipo de Teste   | Métrica                  | Meta                |
|-----------------|--------------------------|---------------------|
| Desempenho      | Tempo de resposta P95    | < 500 ms            |
| Carga           | Throughput sustentado    | > 2000 req/s        |
| Estresse        | Ponto de quebra          | > 15.000 usuários   |
| Escalabilidade  | Eficiência horizontal    | > 80%               |
| Segurança       | Rate limiting            | 100 req/min/IP      |

## Estrutura

```
ex10/
├── tests/
│   ├── test_desempenho.py
│   ├── test_carga.py
│   ├── test_estresse.py
│   ├── test_escalabilidade.py
│   └── test_seguranca.py
├── relatorio.md
└── README.md
```

## Execução

Cada script aceita variáveis de ambiente para configurar a URL alvo e demais parâmetros. Defaults apontam para `https://httpbin.org/get` apenas como exemplo — substitua por sua aplicação:

```bash
BASE_URL=https://meu-ecommerce.com/api/produtos python tests/test_desempenho.py
BASE_URL=https://meu-ecommerce.com/api/produtos python tests/test_carga.py
BASE_URL=https://meu-ecommerce.com/api/produtos python tests/test_estresse.py
BASE_URL_1=https://nodo-1/api BASE_URL_N=https://lb/api N_INSTANCIAS=4 python tests/test_escalabilidade.py
BASE_URL=https://meu-ecommerce.com/api/produtos python tests/test_seguranca.py
```

Cada script retorna **exit code 0** em caso de aprovação e **1** em caso de reprovação, permitindo encadear na pipeline.

## Parâmetros configuráveis (por env var)

| Script                      | Variáveis                                           |
|-----------------------------|-----------------------------------------------------|
| `test_desempenho.py`        | `BASE_URL`, `N_AMOSTRAS`                            |
| `test_carga.py`             | `BASE_URL`, `DURACAO_S`, `N_THREADS`                |
| `test_estresse.py`          | `BASE_URL` (níveis e limite de erro são constantes) |
| `test_escalabilidade.py`    | `BASE_URL_1`, `BASE_URL_N`, `N_INSTANCIAS`, `DURACAO_S`, `THREADS_POR_INSTANCIA` |
| `test_seguranca.py`         | `BASE_URL`                                          |
