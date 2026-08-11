## While ----------------------------
print(1)
print(2)
print(3)

print("=" * 10)

i = 1
while i <= 3:
    print(i)
    i += 1

print("=" * 10)

iii = 20
while iii >= 1:
    print(iii)
    iii -= 2

print("=" * 10)

'''
Exemplo de While infinito:

inf = 1
while inf > 0:
    print(inf)
    inf *= 2
'''

## For ----------------------------
for j in range(5):
    print(j)

print("=" * 10)


for jj in range(2, 5):
    print(jj)

print("=" * 10)

# 0 = início, 12 = limite (não inclui 12), 2 = pula de!
for jjj in range(0, 12, 2):
    print(jjj)

print("=" * 10)

## Break ----------------------------
for ij in range (0, 100):
    print(ij)
    if ij == 5:
        break

print("=" * 10)

while True:
    comando = input("Digite um comando (ou 'sair' para encerrar): ")

    if comando.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    print(f"Você digitou: {comando}")

print("=" * 10)

## Continue ----------------------------
for it in range(1, 25):
    if it % 2 == 0:
        print(f"{it} is even")
    else:
        continue
    print("next iteration")

print("=" * 10)

## Acumulador ----------------------------
texto = "banana"
contador_a = 0

iit = 0
while iit < len(texto):
    if texto[iit] == "a":
        contador_a += 1
    iit += 1

print("Número de letras 'a' na palavra:", contador_a)

print("=" * 10)

soma = 0

for iso in range(1, 11):
    soma += iso

print("A soma dos números de 1 a 10 é:", soma)

print("=" * 10)

## Loops aninhados ----------------------------
for inu in range(1, 11):
    for jno in range(1, 11):
        print(f"{inu} x {jno} = {inu * jno}")
    print("---")

## Exemplo ----------------------------



print("=" * 40)

