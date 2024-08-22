# 5. Escreva um programa que receba uma lista de números do usuário e imprima
# apenas os números pares presentes na lista.

lista =[]

while True:
    numeros = float(input("digite o números de usuários:"))

    lista.append(numeros)
    # print(lista) -----> comentario de verificação
    for numeros in lista:
        if numeros % 2 == 0:
           
            print(f"numeros pares presentes na lista {numeros}")
           