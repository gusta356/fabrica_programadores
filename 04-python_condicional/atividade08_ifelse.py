#autor:gustavo martins 

#projeto:coondicionais

#definição das variáveis
nome= input ("digite seu nome: ")
peso= float(input("digite sua peso: "))
altura= float(input("digite sua altura: "))

imc= peso/(altura*altura)
if imc <=18.5:
    print("esta abaixo do peso! ")
else:
    print("esta peso normal! ")
