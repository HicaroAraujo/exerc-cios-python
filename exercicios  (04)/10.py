#  Verificação de vogal: Escreva um programa que leia uma letra e verifique se ela é uma vogal
# ou não. Se for uma vogal, exiba a mensagem "A letra é uma vogal". Caso contrário, exiba "A
# letra é uma consoante".

letra = input("digite uma letra: ").lower()

 

if letra in "aeiou":
    print(f"A letra {letra} é uma vogal")

else:
    print(f"A letra {letra} é uma consoante")