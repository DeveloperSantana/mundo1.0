velocidade = float(input("Qual a velocidade do carro ?"))
if velocidade > 80:
    print("você foi multado, execedeu 80km/h")
    multa = (velocidade - 80) * 7
    print("você deve pagar {}".format(multa))
print("tenha um bom dia dirija com segurança")
