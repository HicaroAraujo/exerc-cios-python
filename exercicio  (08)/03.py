#  Escreva um programa que solicita ao usuário que digite um número inteiro positivo. O
# programa deve calcular e imprimir a soma de todos os números pares de 1 até o número
# digitado pelo usuário, usando um loop for.


numero = int (input("digite um numero:"))

contador = 0
lista = []
# verifiquei se contador é menor que o numero
while contador < numero:

    contador += 1
    if contador % 2 == 0:
      lista.append(contador)
    soma = sum(lista)
     
print(f"Os numeros pares até o numero digitado são: {lista}")
print(f"E a soma desses numeros pares  é: {soma}")
