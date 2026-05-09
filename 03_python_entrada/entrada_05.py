#autor: gustavo martins
#projeto: entrada com input e f-string

#declaração de variáveis
nome = input("digite seu nome: ")
valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
soma = valor1 / valor2
subtração = valor1 - valor2
multiplicação = valor1 * valor2
divisão = valor1 / valor2

#exibindo os resultados com f-string
print(nome) 
print(f"o resultado da soma é:{soma}")
print(f"o resultado da subtração é "{subtração})
print(f"o resultado da multiplicação "{multiplicação})
print(f"o resultado da divisão é "{divisão})