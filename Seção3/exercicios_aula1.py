## Exercício 1 — Criando variáveis e investigando tipos
nome_Exerc = "Kemilly"
idade_Exerc = 28
altura_Exerc = 1.60
estudante_Exerc = True

print(nome_Exerc) ## Kemilly
print(idade_Exerc) ## 28
print(altura_Exerc) ## 1.60
print(estudante_Exerc) ## True

print(type(nome_Exerc)) ## str
print(type(idade_Exerc)) ## int
print(type(altura_Exerc)) ## float
print(type(estudante_Exerc)) ## bool

print("Nome:", nome_Exerc, "— Tipo:", type(nome_Exerc))
print("Idade:", idade_Exerc, "— Tipo:", type(idade_Exerc))
print("Altura:", altura_Exerc, "— Tipo:", type(altura_Exerc))
print("Estudante:", estudante_Exerc, "— Tipo:", type(estudante_Exerc))

## Exercício 2 — Converta e corrija
valor1 = "50"
valor2 = "23.75"

soma = int(valor1) + float(valor2)
print("Soma:", soma) ## 73.75


## Corrigir:
nome = "Ana"
idade = 30
altura = 1.65

## f-string
print(f"Nome: {nome}") ## Nome: Ana
print(f"Idade: {idade} anos") ## Idade: 30 anos
print(f"Altura: {altura}m") ## Altura: 1.65m

## Concatenação com +
print("Nome: " + nome)
print("Idade: " + str(idade) + " anos")  # int não concatena direto com string
print("Altura: " + str(altura) + "m")    # float também precisa de str()


## Exercício 3 — Verdadeiro ou Falso?
print(bool(42))        # True (número diferente de zero)
print(bool(""))        # False (string vazia)
print(bool(" "))       # True (espaço não é string vazia)
print(bool(0))         # False (zero)
print(bool("False"))   # True (string com conteúdo, mesmo que seja "False")
print(bool(-1))        # True (número diferente de zero)
print(bool(None))      # False (None)


## Exercício 4 — Formulário completo

## "Meu nome é [nome], tenho [idade] anos e trabalho como [profissão]."

name_Exerc = input("Qual o seu nome? ")
idade_Exerc = int(input("Qual a sua idade? "))
trabalho_Exerc = input("Qual a sua profissão? ")

print(f"Meu nome é {name_Exerc}, tenho {idade_Exerc} anos e trabalho como {trabalho_Exerc}.")
