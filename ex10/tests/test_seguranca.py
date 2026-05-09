"""Teste de SEGURANCA - rate limiting.

Meta: ate 100 req/min/IP devem passar; acima disso o servidor deve responder
com 429 (Too Many Requests).
"""

import os
import time
import urllib.request
from urllib.error import HTTPError, URLError

BASE_URL = os.environ.get("BASE_URL", "https://httpbin.org/get")
LIMITE_PERMITIDO = 100
TOTAL_REQ = 150


def disparar(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            return resp.status
    except HTTPError as e:
        return e.code
    except URLError:
        return -1


def main():
    inicio = time.time()
    status_count = {}
    for i in range(TOTAL_REQ):
        s = disparar(BASE_URL)
        status_count[s] = status_count.get(s, 0) + 1

    duracao = time.time() - inicio
    bloqueadas = status_count.get(429, 0)
    permitidas = sum(c for s, c in status_count.items() if 200 <= s < 300)

    # Espera-se: ~LIMITE_PERMITIDO permitidas e (TOTAL_REQ - LIMITE_PERMITIDO) bloqueadas.
    aprovado = (
        permitidas <= LIMITE_PERMITIDO + 5  # tolerancia
        and bloqueadas >= TOTAL_REQ - LIMITE_PERMITIDO - 5
    )

    print(f"Requisicoes: {TOTAL_REQ} em {duracao:.1f}s")
    print(f"Status: {status_count}")
    print(f"Permitidas (2xx): {permitidas}")
    print(f"Bloqueadas (429): {bloqueadas}")
    print(f"Limite esperado: {LIMITE_PERMITIDO}/min")
    print(f"Resultado: {'APROVADO' if aprovado else 'REPROVADO'}")
    return 0 if aprovado else 1


if __name__ == "__main__":
    raise SystemExit(main())
