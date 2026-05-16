#autor:gustavo martins 

#projeto:coondicionais

#definição das variáveis
nome = input ("digite seu nome: ")
idade = float(input("digite sua idade: "))
produto = float(input("digite o preço do produto: "))
if produto >=100:
    preço=produdo *0.10
else:
     preço=produto *0.5
    print("nome:", nome)
    print("idade: ",idade)
    print("valor calculado: ", preço)