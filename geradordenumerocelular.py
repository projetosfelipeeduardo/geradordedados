import random

def gerar_numero_celular():
    # Cria um prefixo de operadora aleatório (exemplo: 9 para celulares no Brasil)
    prefixo = str(random.randint(6, 9))

    # Gera os 8 dígitos restantes aleatoriamente
    numero = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    numeroinicial = "9"

    # Formata o número no padrão de celular do Brasil (exemplo: (99) 99999-9999)
    numero_formatado = f'({prefixo}9) {numeroinicial}{numero[:4]}-{numero[4:]}'

    return numero_formatado

# Exemplo de uso:
for _ in range(5):
    print(gerar_numero_celular())
