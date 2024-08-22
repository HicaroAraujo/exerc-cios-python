# Escreva um programa que solicita ao usuário que digite um número inteiro positivo. O
# programa deve imprimir todos os números de 1 até o número digitado pelo usuário que são
# múltiplos de 3, usando um loop while.


numero = int(input("digite um número inteiro e positivo:"))

contador = 0 
lista = []
while contador < numero:
    contador += 1
    
    if contador % 3 == 0:
        lista.append(contador)

print(f"A lista de numeros multíplos de (3) do 1 até {numero} são: {lista}  ")