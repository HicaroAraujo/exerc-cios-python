# 7. Escreva um programa que solicita ao usuário que digite uma palavra. O programa deve
# verificar se a palavra digitada começa com a letra "A". Se sim, deve imprimir "Começa com
# A"; caso contrário, deve imprimir "Não começa com A".

# dite a palavra
palavra = input("digite uma palavra:")

# se a palavra tiver mais que 0 letras e a primeira letra for igual a letra "A" ou igual "a"
if len(palavra) > 0 and palavra[0] == "A" or palavra[0] == "a":
        print(f"a palavra ({palavra} ) começa com a letra A")

else:
        print(f"A palavra ({palavra})  NÃO começa com a letra A")
   