import random

# Uma lista com 5 nomes
nome = ["Jose", "Marcelo", "Matheus", "Felipe", "Henrique"]
# Uma lista com 5 e-mails
email = ["jose@gmail.com", "marcelo@gmal.com", "matheus@gmail.com", "felipe@gmail.com", "henrique@gmail.com"]
# Uma lista com 5 telefones
telefone = ["(69) 94161-9025", "(99) 93052-6481", "(79) 99784-9790", "(99) 99259-5461", "(79) 98089-9774"]
# Uma lista com 5 cidades
cidades = ["Manaus", "Florianópolis", "Cuiabá", "Belém", "Porto Alegre"]
# Uma lista com 5 estados
estados = ["Piauí", "Santa Catarina", "Rondônia", "Maranhão", "Alagoas"]

print ('''Bem-vindo ao Gerador de Dados de testes - Para finalizar o programa, digite "parar"
-----------------------------------------------
Escolha uma ou mais opções abaixo para serem geradas aleatoriamente
[1] Nome
[2] E-mail
[3] Telefone
[4] Cidade
[5] Estado
''')
while True:
    entrada = input("Digite uma(as) ou mais opções (ou 'parar' para encerrar): ")
    if entrada.lower() == 'parar':
        print("Programa encerrado.")
        break
    if '1' in entrada:
        nome_escolhido = random.choice(nome)
        print(nome_escolhido)
    if '2' in entrada:
        email_escolhido = random.choice(email)
        print(email_escolhido)
    if '3' in entrada:
        telefone_escolhido = random.choice(telefone)
        print(telefone_escolhido)
    if '4' in entrada:
        cidades_escolhido = random.choice(cidades)
        print(cidades_escolhido)
    if '5' in entrada:
        estados_escolhido = random.choice(estados)
        print(estados_escolhido)
    break

while True:
     salvar_arquivo = input("Deseja salvar o Arquivo em Txt? S / N  ")
     if salvar_arquivo.lower() == 's':
         with open('dados_gerados.txt', 'w', encoding='utf-8') as arquivo:
             for i in range(1):  # Supondo que você deseje salvar 5 linhas de dados
                 linha = f"Nome: {nome_escolhido}\nEmail: {email_escolhido}\nTelefone: {telefone_escolhido}\nCidade: {cidades_escolhido}\nEstado: {estados_escolhido}"
                 arquivo.write(linha)
         print("Arquivo salvo com sucesso!")
         break
     elif salvar_arquivo.lower() == 'n':
         break
     else:
         print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
     