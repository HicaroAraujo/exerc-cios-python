# Você está desenvolvendo um programa para calcular a altura máxima e o tempo de queda de um
# objeto em um lançamento vertical. O usuário deve informar a altura inicial do objeto. Assuma que a
# aceleração da gravidade é igual a 9,81 m/s². Escreva um algoritmo que calcule e imprima a 
# o tempo de queda do objeto.


import math 

GRAVIDADE = 9.81

altura_inicial = float(input("digite a altura inicial em metros, do objetivo:"))

tempo = math.sqrt(2 * altura_inicial / GRAVIDADE)
# GRAVIDADE em negrito é para velocidade constante
                  

print(f"o tempo de queda foi de {tempo:.2f}segundos")

velocidade = 0 - GRAVIDADE * tempo

print(f"A velocidade é de {velocidade:.2f} m/s")



