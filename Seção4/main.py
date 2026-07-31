## Operador ----------------------------
a = 10
b = 3 

print(a + b) ## 13
print(a - b) ## 7
print(a * b) ## 30
print(a / b) ## 3.3333333333333335
print(a // b) ## 3
print(a % b) ## 1
print(a**b) ## 1000



## Operador para string ----------------------------
primeiro = "hello"
segundo = "world"
print(primeiro + " " + segundo) ## hello world

line = "____________________________________________________________" 
print(line) ## ____________________________________________________________

line1 = "_" * 60
print(line1) ## ____________________________________________________________



## Ordem dos operadores ----------------------------
resultado = 2 + 3 * 4
print(resultado) ## 20

resultado1 = (2 + 3) * 4
print(resultado1) ## 14

resultado2 = 3 % 2
print(resultado2) ## 1 impar

resultado3 = 8 % 2
print(resultado3) ## 0 par



## Operadores de comparação  ----------------------------
a = 10
b = 5 

print(a == b) ## False
print(a != b) ## True
print(a > b) ## True
print(a < b) ## False
print(a >= b) ## True
print(a <= b) ## False

print(line) ## ____________________________________________________________

c = 10
d = 10

print(c == d) ## True
print(c != d) ## False
print(c > d) ## False
print(c < d) ## False
print(c >= d) ## True
print(c <= d) ## True

print("abacaxi" < "banana")  # True - A comparação é feita em ordem alfabética (ordem lexicográfica). Primeiro compara "a" com "b"; como "a" vem antes de "b", o resultado é True.

print("a" < "b")  # True - A letra "a" vem antes da letra "b" no alfabeto, então o resultado é True.

print("c" < "b")  # False - A letra "c" vem depois da letra "b" no alfabeto, então "c" não é menor que "b".

print("aab" < "aac")  # True - As duas primeiras letras ("a" e "a") são iguais. O Python compara o próximo caractere: "b" vem antes de "c", então o resultado é True.



## Operadores de atribuição  ----------------------------
x = 10

x = x + 5
print(x) ## 15

x = x - 2
print(x) ## 13

print(line) ## ____________________________________________________________

y = 10

y += 5
## y = y - 5  |É a mesma coisa que fazer isso!
print(y) ## 15

y -= 2
## y = y - 2  |É a mesma coisa que fazer isso!
print(y) ## 13



## And e Or  ----------------------------
age = 25
salary = 3000

print(age >= 18 and salary >= 2000) ## True
print(age >= 18 or salary >= 2000) ## True

print(line) ## ____________________________________________________________

age1 = 17
salary1 = 3000

print(age1 >= 18 and salary1 >= 2000) ## False
print(age1 >= 18 or salary1 >= 2000) ## True

print(line) ## ____________________________________________________________

age2 = 18
salary2 = 3000

print(age2 >= 18 and salary2 >= 5000) ## False
print(age2 >= 18 or salary2 >= 2000) ## True



## Not  ----------------------------
rain = True
print(rain) ## True

print(line) ## ____________________________________________________________

rain1 = True
print(not rain1) ## False
rain2 = False
print(not rain2) ## True



## Combinação de operadores  ----------------------------
age3 = 20
student = True
salary3 = 1500

print(age3 >= 18 and (student or salary3 > 2000)) ## True 

print(line) ## ____________________________________________________________

age4 = 20
student1 = False
salary4 = 2100

print(age4 >= 18 and (student1 or salary4 > 2000)) ## True

print(line) ## ____________________________________________________________

age5 = 17
student2 = False
salary5 = 2100

print(age5 >= 18 and (student2 or salary5 > 2000)) ## False
