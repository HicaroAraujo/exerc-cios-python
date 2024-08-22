#  Escreva um programa que solicita ao usuário que digite um número positivo. Em seguida, o
# programa deve imprimir todos os números de 1 até o número digitado pelo usuário, usando
# um loop while.

numero = int(input("digit um número positivo:"))

contador = 0

while contador < numero:
    contador +=1
    print(contador)