#autor:gustavo martins 
##autor:gustavo martins
#projeto:coondicionais

#definição das variáveis
nome = input ("digite seu nome: ")
idade = float(input("digite sua idade: "))
def calcular(idade):
    if idade >= 18:
        print("maior de idade!")
    else:
        print("menor de idade!")
calcular(idade)