## Váriaveis

name = "maria"
age = 30
height = 1.65
student = True

_student = False
value1 = 10
value = 10

Name = "John"

full_name = "Stephany Batista"

print(name)

age = 25
year = 2024
temperature = -3

height = 1.75
name = "Alice"

student = False

print(type(age)) # Output <class 'int'> 
print(type(year)) # Output <class 'int'> 
print(type(temperature)) # Output <class 'int'> 
print(type(height)) # Output <class 'float'> 
print(type(name)) # Output <class 'str'> 
print(type(student)) # Output <class 'bool'> 


## Conversão:

age = 25
age2 = 30
name = "Alice"

temp = age + age2
print(temp)

temp2 = name + " teste"
print(temp2)

temp3 = name +" is " + str(age)
print(temp)

""" Não posso fazer nenhuma dessas operações pois retorna erro: 
print(name + " is" + age)

temp = age + name
print(temp)
"""

age3 = "15"
age4 = 10
name2 = "Alice2"

temp4 = int(age3) + age4
print(temp4)

name = "Alice"
age = 30
student = True

print(f"{name} is {age} years old and is a student: {student}")

"""
A f-string é uma forma de formatar strings em Python.
Ela permite inserir variáveis e expressões usando chaves {},
sem precisar concatenar com o operador +.
"""

## Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print (f"{name} is {age} years old")


base = float(input("Base: "))
height = float(input("Height "))
area = base * height

print (f"area is {area}")
