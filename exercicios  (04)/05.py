#  Verificação de número positivo: Escreva um programa que leia um número e verifique se ele
#  é positivo ou negativo. Se for positivo, exiba a mensagem "O número é positivo". Caso
#  contrário, exiba "O número é negativo".

numero = int(input("digite um número:"))

if numero > 0:
    print(f"O número {numero} é positivo!")
elif numero == 0:
    print(f"O número {numero} é neutro")
else: 
    print(f"O número {numero} é negativo")