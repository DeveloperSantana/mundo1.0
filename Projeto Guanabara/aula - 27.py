n = str(input('digite o seu nome completo: ')).strip()
nome = n.split()
print("seu primeiro nome é {}".format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
