# Algoritmo de Tabuada: Desenvolver um programa em Python que permita ao usuário calcular a
# tabuada de qualquer número inteiro. O programa deve solicitar ao usuário que insira um número e, em
#  seguida, exibir a tabuada correspondente de 1 a 10.

numero = int(input("digite um número inteiro:"))
print(f"Tabuada de 0 a 10 do número {numero}:")
contador = 0

while contador < 11:
    print(f"{contador} x {numero} = {contador * numero }")
    contador += 1

  




