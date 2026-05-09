#autor: gustavo martins
#projeto: entrada imc com input e f-string

#declaração de variáveis
nome = input("digite seu nome ")
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
imc = peso / (altura * altura)

#exibindo os resultados 
print(f"---bem vindo---{nome}")
print(f" seu imc é: {imc:.2f}")