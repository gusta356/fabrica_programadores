#autor:gustavo martins
#projeto:coondicionais

#definição das variáveis
nome = input ("digite seu nome: ")
nota = float(input("digite sua nota: "))
def calcular(nota):
    if nota >= 6:
        print("aluno aprovado!")
    else:
        print("aluno reprovado")
calcular(nota)
    