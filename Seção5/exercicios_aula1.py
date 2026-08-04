## Exercício 1 — Classificador de idade ----------------------------
idade = int(input("Qual sua idade? "))

if idade <= 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Vc é criança.")
elif idade <= 17:
    print("Você é adolecente.")
elif idade <= 59:
    print("Você é adulto.")
else:
    print("Você é idoso")

print("=" * 40)


## Exercício 2 — Calculadora com menu ----------------------------
number_1 = float(input("Qual o primeiro número? "))
number_2 = float(input("Qual o segundo número? "))
operation = input("Digite a operação (+, -, *, /):  ")

if operation == "+":
    print(f"Resultado: {number_1 + number_2}")
elif operation == "-":
    print(f"Resultado: {number_1 - number_2}")
elif operation == "*":
    print(f"Resultado: {number_1 * number_2}")
elif operation == "/":
    if number_2 == 0: 
        print("Erro: divisão por zero!")
    else:
        print(f"Resultado: {number_1 / number_2}")
else:
    print("Operação inválida")


print("=" * 40)


## Exercício 3 — Triângulo válido ----------------------------
value_1 = float(input("Qual o primeiro valor do triângulo? "))
value_2 = float(input("Qual o segundo valor do triângulo? "))
value_3 = float(input("Qual o terceiro valor do triângulo? "))


if value_1 < value_2 + value_3 and value_2 < value_1 + value_3 and value_3 < value_1 + value_2:
    if value_1 == value_2 == value_3:
        print("Temos um triângulo: Equilátero")
    elif value_1 == value_2 or value_1 == value_3 or value_2 == value_3:
        print("Temos um triângulo: Isósceles")
    else:
        print("Temos um triângulo: Escaleno")
else:
    print("Não forma um triângulo")


print("=" * 40)


## Exercício 4 — Faixa salarial de imposto ----------------------------
salario_bruto = float(input("Qual o valor do seu salário bruto? "))


if salario_bruto <= 1900.00:
    percentual = 0
elif salario_bruto <= 2800.00:
    percentual = 7.5
elif salario_bruto <= 3750.00:
    percentual = 15
elif salario_bruto <= 4600.00:
    percentual = 22.5
else:
    percentual = 27.5

calculo_total = salario_bruto * (percentual / 100)
liquido = salario_bruto - calculo_total

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Percentual: {percentual}%")
print(f"Desconto: R$ {calculo_total:.2f}")
print(f"Salário líquido: R$ {liquido:.2f}")

