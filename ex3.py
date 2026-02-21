def calcular_frete_base(peso):
    frete = 0

    if 0 >= peso > 20:
        raise ValueError("Peso inválido")
    
    if peso <= 1:
        frete = 10
    elif peso <= 5:
        frete = 15
    elif peso <= 20:
        frete = 25

    return frete

def calcular_acrescimo(destino):
    if destino == "nacional mesma região":
        return 1
    elif destino == "nacional outra região":
        return 1.5
    elif destino == "nacional outra região":
        return 2
    
def calcular_frete(peso, destino, valor_pedido):
    is_frete_gratis = valor_pedido > 200

    if is_frete_gratis:
        return 0
    
    frete_base = calcular_frete_base(peso)
    acrescimo = calcular_acrescimo(destino)

    return frete_base * acrescimo

