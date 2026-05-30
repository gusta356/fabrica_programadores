#autor:gustavo martins oliveira 
#projeto:loop FOR

numero = int(input("digite a tabuada desejada: "))
inicio = int(input("digite o primeiro numero da tabuada: "))
fim = int(input("digite o ultimo numero da tabuada: "))

for i in range(inicio,fim+1):
    print(f" {numero} x {i} = {numero * i}")

