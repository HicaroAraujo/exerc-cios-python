#Escreva um programa que receba uma lista de números do usuário e verifique se
# um número específico está presente na lista.

numeros = input("digite uma lista de numeros separadas por espaço:").split()

numeros = [int(numero) for numero in numeros]

verificar_numero = int(input("digite o numero para verificar se eles estão na lista:"))

if verificar_numero in numeros:
    print(f"O numero {verificar_numero} esta presente na lista!")

else:
    print(f"o numero {verificar_numero} não está presente na lista:")