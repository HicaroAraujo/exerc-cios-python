# Ana é uma professora de matemática que está desenvolvendo um programa para calcular a média
# aritmética de uma lista de números. Ela sabe que, para calcular a média, é necessário somar todos
# os números da lista e dividir pelo total de números. Ana quer desenvolver um programa em Python
# que possa ser utilizado por seus alunos para facilitar esse processo. Escreva um algoritmo que ajude
# Ana a calcular a média aritmética de uma lista de números


lista = []
contador = 0 
while True:
    numero = int (input("digite suas notas, separados por virgula:"))

    lista.append(numero)
     
    quantidade = len(lista)
    
    soma = sum(lista)


    media = soma / quantidade

   
    print(f"qauntidade de notas : {quantidade}")
    print(f"listas das notas: {lista}")
    print(f"A soma das notas: {soma}")
    print(f" A MÉDIA DAS NOTAS É : {media}")