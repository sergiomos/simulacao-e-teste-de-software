def sanatized(cpf):
    return str(cpf).replace(".", "").replace("-", "")

def validar_cpf(cpf):
    cpf_sanitizado = sanatized(cpf);
    cpf_digits = cpf_sanitizado[0:9]
    check_digits = cpf_sanitizado[9:11]

    return len(cpf_sanitizado) == 11

def formatar_cpf(cpf):
    sCPF = sanatized(cpf)
    return f"{sCPF[0:3]}.{sCPF[3:6]}.{sCPF[6:9]}-{sCPF[9:11]}"

print(formatar_cpf(48353476843))