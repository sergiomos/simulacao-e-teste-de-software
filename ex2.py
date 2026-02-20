def sanatized(cpf):
    return str(cpf).replace(".", "").replace("-", "")


def validar_cpf(cpf: str) -> bool:
    cpf_sanitizado = sanatized(cpf)

    has_only_digits = cpf_sanitizado.isdigit()
    has_length_11 = len(cpf_sanitizado) == 11
    all_digits_same = len(set(cpf_sanitizado)) == 1
    
    if not has_only_digits or not has_length_11 or all_digits_same:
        return False
    
    cpf_digits = cpf_sanitizado[0:9]
    check_digits = cpf_sanitizado[9:11]
    
    soma = sum(int(cpf_digits[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto
    
    cpf_com_primeiro = cpf_digits + str(primeiro_digito)
    soma = sum(int(cpf_com_primeiro[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto
    
    dígitos_calculados = str(primeiro_digito) + str(segundo_digito)
    return check_digits == dígitos_calculados


def formatar_cpf(cpf: str) -> str:
    if not validar_cpf(cpf):
        raise ValueError(f"CPF inválido: {cpf}")
    
    sCPF = sanatized(cpf)
    return f"{sCPF[0:3]}.{sCPF[3:6]}.{sCPF[6:9]}-{sCPF[9:11]}"