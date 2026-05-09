"""Teste de ESTRESSE - ponto de quebra.

Meta: ponto de quebra > 15.000 usuarios simultaneos sem degradacao critica.
Define-se "quebra" como taxa de erro >= 5% no nivel de concorrencia testado.
"""

import os
import threading
import time
import urllib.request
from urllib.error import URLError

BASE_URL = os.environ.get("BASE_URL", "https://httpbin.org/get")
META_USUARIOS = 15_000
NIVEIS = [1_000, 5_000, 10_000, 15_000, 20_000]
LIMITE_ERRO = 0.05  # 5%


def worker(contador, lock):
    try:
        with urllib.request.urlopen(BASE_URL, timeout=5) as resp:
            resp.read()
        with lock:
            contador[0] += 1
    except (URLError, TimeoutError, OSError):
        with lock:
            contador[1] += 1


def rodar_nivel(usuarios):
    contador = [0, 0]
    lock = threading.Lock()
    threads = [threading.Thread(target=worker, args=(contador, lock)) for _ in range(usuarios)]
    inicio = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    duracao = time.time() - inicio
    total = contador[0] + contador[1]
    taxa_erro = contador[1] / total if total else 1.0
    return duracao, contador[0], contador[1], taxa_erro


def main():
    ponto_quebra = None
    print(f"{'Usuarios':>10} | {'Duracao':>8} | {'OK':>6} | {'Erros':>6} | {'%Erro':>6}")
    print("-" * 56)
    for n in NIVEIS:
        d, ok, err, taxa = rodar_nivel(n)
        print(f"{n:>10} | {d:>7.1f}s | {ok:>6} | {err:>6} | {taxa*100:>5.1f}%")
        if taxa >= LIMITE_ERRO and ponto_quebra is None:
            ponto_quebra = n

    if ponto_quebra is None:
        ponto_quebra = NIVEIS[-1] + 1  # nao quebrou no maior nivel testado
    aprovado = ponto_quebra > META_USUARIOS
    print(f"\nPonto de quebra estimado: {ponto_quebra} usuarios (meta > {META_USUARIOS})")
    print(f"Resultado: {'APROVADO' if aprovado else 'REPROVADO'}")
    return 0 if aprovado else 1


if __name__ == "__main__":
    raise SystemExit(main())
