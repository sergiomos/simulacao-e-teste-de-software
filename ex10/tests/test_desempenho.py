"""Teste de DESEMPENHO - tempo de resposta P95.

Meta: P95 < 500 ms.
"""

import os
import statistics
import time
import urllib.request
from urllib.error import URLError

BASE_URL = os.environ.get("BASE_URL", "https://httpbin.org/get")
N_AMOSTRAS = int(os.environ.get("N_AMOSTRAS", "100"))
META_P95_MS = 500


def medir(url):
    inicio = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            resp.read()
    except URLError:
        return None
    return (time.perf_counter() - inicio) * 1000


def percentil(amostras, p):
    ordenado = sorted(amostras)
    k = int(len(ordenado) * p / 100) - 1
    return ordenado[max(k, 0)]


def main():
    tempos = []
    for _ in range(N_AMOSTRAS):
        t = medir(BASE_URL)
        if t is not None:
            tempos.append(t)

    if not tempos:
        print("FALHA: nenhuma resposta valida coletada")
        return 1

    p95 = percentil(tempos, 95)
    media = statistics.mean(tempos)
    aprovado = p95 < META_P95_MS

    print(f"Amostras coletadas: {len(tempos)}/{N_AMOSTRAS}")
    print(f"Tempo medio: {media:.1f} ms")
    print(f"P95: {p95:.1f} ms (meta < {META_P95_MS} ms)")
    print(f"Resultado: {'APROVADO' if aprovado else 'REPROVADO'}")
    return 0 if aprovado else 1


if __name__ == "__main__":
    raise SystemExit(main())
