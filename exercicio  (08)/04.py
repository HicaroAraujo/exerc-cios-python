# Escreva um programa que solicita ao usuário que digite uma frase. O programa deve contar
# e imprimir quantas vogais (a, e, i, o, u) a frase possui.

frase = input("digite uma frase:")

contador = 0

vogais = "aeiouAEIOU"

for letra in frase:

    if letra in vogais:
      
      contador += 1

print(f"A frase contem {contador} vogais")



