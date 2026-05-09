"""Teste de ESCALABILIDADE - eficiencia horizontal.

Compara throughput com N instancias contra throughput com 1 instancia:
    eficiencia = (rps_N / N) / rps_1

Meta: eficiencia > 80%.
"""

import os
import threading
import time
import urllib.request
from urllib.error import URLError

BASE_URL_1 = os.environ.get("BASE_URL_1", "https://httpbin.org/get")
BASE_URL_N = os.environ.get("BASE_URL_N", "https://httpbin.org/get")
N_INSTANCIAS = int(os.environ.get("N_INSTANCIAS", "2"))
DURACAO_S = int(os.environ.get("DURACAO_S", "10"))
THREADS_POR_INSTANCIA = int(os.environ.get("THREADS_POR_INSTANCIA", "20"))
META_EFICIENCIA = 0.80


def worker(url, parar_em, contador, lock):
    while time.time() < parar_em:
        try:
            with urllib.request.urlopen(url, timeout=5) as resp:
                resp.read()
            with lock:
                contador[0] += 1
        except URLError:
            with lock:
                contador[1] += 1


def medir_rps(url, n_threads, duracao_s):
    contador = [0, 0]
    lock = threading.Lock()
    parar_em = time.time() + duracao_s
    threads = [threading.Thread(target=worker, args=(url, parar_em, contador, lock)) for _ in range(n_threads)]
    inicio = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return contador[0] / (time.time() - inicio)


def main():
    rps_1 = medir_rps(BASE_URL_1, THREADS_POR_INSTANCIA, DURACAO_S)
    rps_n = medir_rps(BASE_URL_N, THREADS_POR_INSTANCIA * N_INSTANCIAS, DURACAO_S)
    eficiencia = (rps_n / N_INSTANCIAS) / rps_1 if rps_1 else 0
    aprovado = eficiencia > META_EFICIENCIA

    print(f"RPS com 1 instancia: {rps_1:.1f}")
    print(f"RPS com {N_INSTANCIAS} instancias: {rps_n:.1f}")
    print(f"Eficiencia horizontal: {eficiencia*100:.1f}% (meta > {META_EFICIENCIA*100:.0f}%)")
    print(f"Resultado: {'APROVADO' if aprovado else 'REPROVADO'}")
    return 0 if aprovado else 1


if __name__ == "__main__":
    raise SystemExit(main())
