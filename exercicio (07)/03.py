# 3. Escreva um programa que receba uma lista de números do usuário e calcule a
# soma de todos os números presentes na lista.

lista = []

while True:
    numeros = int(input("digite um Número:"))
    
    lista.append(numeros)
     # coloquei os numeros dentro da lista
    
    soma = sum(lista)

    print(f"Por enquanto a soma de todos os  numeros digitados é {soma}")