#  Conversão de Inteiro para Binário: Desenvolver um programa em Python que converta um número
# inteiro fornecido pelo usuário em sua representação binária.
# Descrição:
#     O programa deve solicitar ao usuário que insira um número inteiro.
#     O programa deve então converter esse número inteiro em sua representação binária sem usar a
#     função built-in(Função Interna) bin().
#     Exibir o resultado da conversão.

numero = int(input("digite um numero:"))
binario = 0
posicao = 1

while numero > 0:
    digito = numero % 2
    print(digito)
    binario += digito * posicao
    numero //= 2
    posicao *= 10
  
    print("A representação binária é:", binario)
    break
