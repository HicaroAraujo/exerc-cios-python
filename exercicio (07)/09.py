#  Escreva um programa que receba uma lista de números do usuário e imprima a
# lista em ordem decrescente.

numeros = input("digite uma lista de NÚMEROS separadas por espaços:").split()

# para cada numero dentro da lista numeros colocar valor inteiro 
numeros = [int(numero) for numero in numeros]

# converte a lista para orderm decrescente
numeros.sort(reverse = True)

print(numeros)
    
