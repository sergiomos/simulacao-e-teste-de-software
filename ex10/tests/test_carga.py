import os
import threading
import time
import urllib.request
from urllib.error import URLError

BASE_URL = os.environ.get("BASE_URL", "https://httpbin.org/get")
DURACAO_S = int(os.environ.get("DURACAO_S", "10"))
N_THREADS = int(os.environ.get("N_THREADS", "50"))
META_RPS = 2000


def worker(parar_em, contador, lock):
    while time.time() < parar_em:
        try:
            with urllib.request.urlopen(BASE_URL, timeout=5) as resp:
                resp.read()
            with lock:
                contador[0] += 1
        except URLError:
            with lock:
                contador[1] += 1


def main():
    contador = [0, 0]  # [sucesso, falha]
    lock = threading.Lock()
    parar_em = time.time() + DURACAO_S

    threads = [
        threading.Thread(target=worker, args=(parar_em, contador, lock))
        for _ in range(N_THREADS)
    ]
    inicio = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    duracao = time.time() - inicio

    rps = contador[0] / duracao
    aprovado = rps > META_RPS

    print(f"Threads: {N_THREADS} | Duracao: {duracao:.1f}s")
    print(f"Sucesso: {contador[0]} | Falhas: {contador[1]}")
    print(f"Throughput: {rps:.1f} req/s (meta > {META_RPS} req/s)")
    print(f"Resultado: {'APROVADO' if aprovado else 'REPROVADO'}")
    return 0 if aprovado else 1


if __name__ == "__main__":
    raise SystemExit(main())
