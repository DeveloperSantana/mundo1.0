import random
n1 = str(input("digite o primeiro aluno: "))
n2 = str(input('digite o segundo aluno: '))
n3 = str(input('digite o terceiro aluno:'))
n4 = str(input("digite o quarto aluno: "))
lista = [n1, n2,n3,n4]
random.shuffle(lista)
print("a ordem de apresentação será")
print(lista)

