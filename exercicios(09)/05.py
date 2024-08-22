# 5) Verificação de Produtos
# A loja de eletrônicos de TechVille queria verificar se um determinado produto estava em estoque
# (representados por números inteiros), além de saber quantos produtos pares e ímpares eles tinham. Eles
# recorreram aos Pythonistas para criar um programa que pudesse fazer essas verificações.

# pedir lista de numeros inteiros que repesentam os produtos
pares = []
impares = []

# enquanto for verdade peça lista de numero, coloque eles para valores inteiros e paça um numero prara verificação de lista
while True:
    lista_numeros = input("digite uma lista de produtos representados por NÚMEROS INTEIROS, separado por espaço, por favor: ").split()
    lista_numeros = [int(numero) for numero in lista_numeros]

    # pedir numero para verifcação no estoque 
    verificacao = int(input("digite o número para verificar se ele esta na lista: "))

# para cada numeros dentro da lista solicitada verificar se o numero é divisivel por 2, logo após coloca-lo dentro da lista pares 
    for numeros in lista_numeros:
                
        if numeros % 2 == 0:
            pares.append(numeros)
            soma = len(pares) 
# para cada numeros verfica se ele é divisivel por 3, logo após coloca-lo dentro da lista ímpares
        if numeros % 2 != 0:
                impares.append(numeros)
                soma_impa = len(impares)

            
# verfica se o numero de verificação esta presente na lista
    if verificacao in lista_numeros:
 # se SIM apresntar na tela numero de verificaçaõ, a contagem dos pares e contagens dos impares:   
     print(f"o {verificacao} está na lista, tendo na lista {soma_impa} números ímpares e {soma} números pares!")

# se NÃO , dizer que o numero de verificação não esta na lksta e printar a contagem de pares e impares
    else:
         print(f"o {verificacao} não está na lista, tendo na lista {soma_impa} números ímpares e {soma} números pares!")


      





