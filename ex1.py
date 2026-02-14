def validar_nota(nota):
    return nota >= 0 and nota <= 10

def calcular_media(notas):
    if not len(notas):
        raise ValueError("Não há notas para calcular a média")

    soma = 0
    quantidade_de_notas = 0

    for nota in notas:
        if validar_nota(nota):
            soma += nota
            quantidade_de_notas += 1

    return soma / quantidade_de_notas


def obter_situacao(media):
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    elif media < 5:
        return "REPROVADO"
    else:
        raise ValueError("Média inválida")

def filtrar_por_situacao(notas, situacao):
    return [nota for nota in notas if obter_situacao(nota) is situacao]


def calcular_estatisticas(notas):
    return {"media": calcular_media(notas),
            "maior": max(notas),
            "menor": min(notas),
            "aprovados": len(filtrar_por_situacao(notas, "APROVADO")),
            "reprovados": len(filtrar_por_situacao(notas, "REPROVADO")),
            "recuperacao": len(filtrar_por_situacao(notas, "RECUPERAÇÃO"))}


def normalizar_nota(notas, nota_maxima):
    fator_de_normalizacao = 10
    return [nota * nota_maxima / fator_de_normalizacao for nota in notas]
=======
def calcular_media(notas):
    if not len(notas):
        raise ValueError("Não há notas para calcular a média")

    soma = 0
    quantidade_de_notas = 0

    for nota in notas:
        if validar_nota(nota):
            soma += nota
            quantidade_de_notas += 1

    return soma / quantidade_de_notas


def obter_situacao(media):
    if not validar_nota(media):
        raise ValueError("Média inválida")

    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    elif media < 5:
        return "REPROVADO"
    

def filtrar_por_situacao(notas, situacao):
    return [nota for nota in notas if obter_situacao(nota) is situacao]


def calcular_estatisticas(notas):
    return {"media": calcular_media(notas),
            "maior": max(notas),
            "menor": min(notas),
            "aprovados": len(filtrar_por_situacao(notas, "APROVADO")),
            "reprovados": len(filtrar_por_situacao(notas, "REPROVADO")),
            "recuperacao": len(filtrar_por_situacao(notas, "RECUPERAÇÃO"))}


def normalizar_nota(notas, nota_maxima):
    fator_de_normalizacao = 10
    return [nota * nota_maxima / fator_de_normalizacao for nota in notas]
>>>>>>> e18422d2e6a78b1ee895886574cf93f79414a826