#  Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números ímpares presentes na lista.

lista = []

while True:
    numero = int(input("digite o número de usuários:"))

    lista.append(numero)

    for numero in lista:
        if numero % 2 != 0:
         print(f" ímpares presentes na lista {numero} ")