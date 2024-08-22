#  Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números que são múltiplos de 3 e 5 simultaneamente.


while True:
    numeros = input("digite o número de usuários:").split()
    numeros = [int(numero1) for numero1 in numeros]
    
 
    for numero in numeros:
     if numero % 3 == 0 and numero % 5 == 0:

        print(f" número divisivel por 3 e por 5 presente na lista:{numero} ")
        