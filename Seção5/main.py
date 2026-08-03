## If, Elif e Else ----------------------------
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
    print("Pode votar e dirigir.")
elif idade >= 16:
    print("Você é quase maior de idade.")
    print("Pode votar, mas não pode dirigir.")
elif idade >= 14:
    print("Você é adolescente.")
    print("Não pode votar nem dirigir, mas pode trabalhar.")
else:
    print("Você é menor de idade.")
    print("Não pode votar nem dirigir.")

print("Fim do programa.")

line1 = "_" * 20
print(line1) ## ____________________

qual_idade = int(input("Qual a sua idade? "))

if qual_idade >= 18:
    print("Você é maior de idade.")
    print("Pode votar e dirigir.")
elif qual_idade >= 16:
    print("Você é quase maior de idade.")
    print("Pode votar, mas não pode dirigir.")
elif qual_idade >= 14:
    print("Você é adolescente.")
    print("Não pode votar nem dirigir, mas pode trabalhar.")
else:
    print("Você é menor de idade.")
    print("Não pode votar nem dirigir.")

print("Fim do programa.")


line = "_" * 80
print(line) ## ____________________________________________________________


## Condições compostas ----------------------------
idade1 = 20
renda = 3000

if idade1 >= 18 and renda >= 2500:
    print("Você é elegível para empréstimo.")
else:
    print("Desculpe, você não atende aos critérios para o empréstimo.")

print("Fim do programa.")


print(line1) ## ____________________

dia = "sabado"

if dia == "sabado" or dia == "domingo":
    print("Hoje é dia de descanso!")
else:
    print("Hoje é dia de trabalho!")


print(line) ## ____________________________________________________________


## Condições aninhadas ----------------------------
idade2 = 20
tem_carteira = True

if idade2 >= 18:
    print("Você é maior de idade.")
    if tem_carteira:
        print("Você pode dirigir.")
    else:
        print("Você precisa de uma carteira de motorista para dirigir.")
else:
    print("Você é menor de idade.")


print(line1) ## ____________________


idade3 = 20
tem_carteira1 = True

if idade3 >= 18 and tem_carteira1:
    print("Você pode dirigir.")


print(line) ## ____________________________________________________________


## If ternário ----------------------------
idade4 = 20
tem_carteira2 = True

mensagem = "Pode dirigir." if idade4 >= 18 and tem_carteira2 else "Você não pode dirigir."
print(mensagem)


print(line) ## ____________________________________________________________

## Validações de variáveis ----------------------------
nome = input("Digite seu nome: ")

if nome:
    print(f"Olá, {nome}!")
else:
    print("Nome obrigatório.")
