numero = int(input("digite o numero da tabuada: "))
inicio = int(input("digite o primeiro numero: "))
fim = int(input("digite ultimo numero: "))

i = 1

while i <= fim:
    print(f"{numero} x {i} = {numero * i}")
    i = i +1