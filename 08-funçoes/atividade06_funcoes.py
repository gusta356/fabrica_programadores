#autor: gustavo martins
#projeto: entrada com input

#declaração de variáveis
valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))

#função calcular - 4 operações básicas
def calcular(valor1,valor2):
    somar = valor1+valor2
    subtrair = valor1-valor2
    multiplicar = valor1*valor2
    dividir = valor1/valor2
    print(f"o resultado da soma é: {somar}")
    print(f"o resultado da soma é: {subtrair}")
    print(f"o resultado da soma é: {multiplicar}")
    print(f"o resultado da soma é: {dividir}")
   

#chamada da função 
calcular(valor1,valor2)