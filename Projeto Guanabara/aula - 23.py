num = int(input("inofrme um número:"))
u = num // 1 % 10
d  = num // 10 % 10
c  = num // 100 % 100
m  = num // 100 % 100
print("analisando o numero {}".format(num))
print("unidade: ".format(u))
print("dezena: ".format(d))
print("centena: ".format(c))
print("milhar: ".format(m))
