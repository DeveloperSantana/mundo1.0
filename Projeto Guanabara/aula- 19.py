import random
n1 = str(input("digite o primeiro aluno"))
n2 = str(input('digite o segundo aluno'))
n3 = str(input('digite o terceiro aluno'))
n4 = str(input("digite o quarto aluno"))
lista = [n1, n2 , n3 ,n4]
escolhido = random.choice(lista)
print("o aluno  escolhido foi {}".format(escolhido))

