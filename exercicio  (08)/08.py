#  Escreva um programa que solicita ao usuário que digite um número inteiro positivo. O
# programa deve imprimir todos os números de 1 até o número digitado pelo usuário que são
# múltiplos de 2, usando um loop while.


numero = int(input("digite um número inteiro e positivo:"))

contador = 0 
lista = []
while contador < numero:
    contador += 1
    # print(contador)

    if contador % 2 == 0:
       lista.append(contador)
       
print(lista)