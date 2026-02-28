def calcular_frete_base(peso):
    if peso <= 0 or peso > 20:
        raise ValueError("Peso inválido")

    if peso <= 1:
        return 10
    elif peso <= 5:
        return 15
    return 25


def calcular_acrescimo(destino):
    if destino == "mesma região":
        return 1
    elif destino == "outra região":
        return 1.5
    else:
        raise ValueError("Destino inválido")
    

def calcular_frete(peso, destino, valor_pedido):
    if valor_pedido < 0:
        raise ValueError("Valor do pedido inválido")

    if valor_pedido > 200:
        return 0.0
    
    frete_base = calcular_frete_base(peso)
    acrescimo = calcular_acrescimo(destino)

    return frete_base * acrescimo

