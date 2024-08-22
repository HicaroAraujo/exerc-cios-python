#  Escreva um programa que solicita ao usuário que digite uma palavra. O programa deve
# verificar se a palavra digitada possui mais de 5 caracteres. Se sim, deve imprimir a palavra
# em maiúsculas; caso contrário, deve imprimir a palavra em minúsculas.
while True:
    palavra = input("digite uma palavra:")

    if len(palavra) > 5: 
     print(palavra.upper())
    else:
     print(palavra.lower())
    