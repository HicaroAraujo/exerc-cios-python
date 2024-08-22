# 4. Escreva um programa que receba uma lista de números do usuário e calcule a
#  média de todos os números presentes na lista.
lista = []
contador = 0
while True:
    numeros = int(input("digite 0 Número de usuarios:"))
    
    lista.append(numeros)
     # coloquei os numeros dentr0 da lista
    
    soma = sum(lista)
    # somei o os numeros da lista

    contador += 1
    # print(contador) -----> comentario de verificação
     
    media = soma / contador
    # fiz a media dos numeros dentro da lista
    print(f"Por enquanto a média dos numeros presesntes na lista é {media}")

  