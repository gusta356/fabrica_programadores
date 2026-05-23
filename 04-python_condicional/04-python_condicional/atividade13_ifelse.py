#autor:gustavo martins 

#projeto:coondicionais

#definição das variáveis
nome= input ("digite seu nome: ")
peso= float(input("digite sua peso: "))
altura= float(input("digite sua altura: "))

imc= peso/(altura*altura)
if imc <=18.5:
    print("seu imc esta abaixo da taabela ")
elif imc >=25.9:
    print("seu imc esta agradavel ")
elif imc >=29.9:
    print("voce esta acima do peso ")
elif >=34.9:
    print("voce se encontra em obsidade I ")
elif imc >=39.9:
    print("voce se encontra em obsidade grau II")
else:
    print("voce se em obsidade grau III procure um medico ")