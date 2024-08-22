#  Escreva um programa que solicita ao usuário que digite uma sequência de números
# positivos, um de cada vez. O programa deve calcular e imprimir a média desses números.
lista = []

while True:
    numero = int(input("digite um número inteiro e positivo:"))
    

    if numero > 0 : 
     lista.append(numero)

     soma = sum(lista)
     quantidade = len(lista) 

     media = soma/ quantidade
    
     
    

    print(f"A lista de numeros positivo digitadas é : {lista}")
    # print(quantidade)  -----> verificação
    # print(soma) -----> verificação
    print(f"a média dos numeros até agora é : {media}")
     
