from random import randint

computador = randint(0,5) #sorteio e númerro
print("vou pensar em um número de 0 a 5, tente adivinhar")
print('-=-' * 20)
jogador = int(input("digite um número"))
print('-=-' * 20)
print("pensei no numero {}'".format(computador))
if jogador == computador:
    print("parabens ! venceu ")
else:
    print("eu ganhei ")

