# 2. Escreva um programa que receba uma lista de nomes do usuário e imprima cada
#  nome em uma linha separada.

lista = []

while True:
    nome = input("digite seu nome:")

    lista.append(nome)

    for nome in lista:
        print(nome)