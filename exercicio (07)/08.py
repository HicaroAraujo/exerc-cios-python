# Escreva um programa que receba uma lista de números do usuário e imprima a
# lista em ordem crescente.

numeros = input("digite uma lista NÚMEROS seradas por espaço:").split()
# split >>> torna a lista numa lista de verdade

numeros = [int(numero) for numero in numeros]
# para cada numero da lista numeros deixe eles inteiros 

ordem = sorted(numeros)
# uma nova variavel recebe lista ordenada

print(f"Lista ordenada: {ordem}")