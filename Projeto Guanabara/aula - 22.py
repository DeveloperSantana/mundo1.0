nome = str(input("digite o seu nome completo: ")).strip()
print("analisando o seu nome...")
print("seu nome em maiusculas é {}".format(nome.upper()))
print("seu nome em minuscula é {}".format(nome.lower()))
print("seu nome em minuscula é {} letras".format(len(nome)-nome.count(" ")))
print("seu primeiro nome tem {} letras".format(nome.find('')))


