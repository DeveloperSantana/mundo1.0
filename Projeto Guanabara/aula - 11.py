prod = float(input(" digite o valor do seu produto:" ))
nvvalor =  prod / 100
porcent = nvvalor * 5
valor = prod - porcent

print(" o novo valor com 5 por cento de desconto é {} ".format(valor))

#ou prod - (prod * 5 / 100)