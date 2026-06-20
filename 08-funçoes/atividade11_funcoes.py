#autor:gustavo martins oliveira 
#projeto:loop FOR

numero = int(input("digite um numero "))

def somar(numero):
    for i in range(1,11):
        print(f" {numero} x {i} = {numero * i}")
somar(numero)