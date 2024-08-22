# Você está desenvolvendo um programa para calcular a distância percorrida por um objeto em um
# movimento uniformemente acelerado. O usuário deve informar a velocidade inicial, a aceleração e o
# tempo de deslocamento. Escreva um algoritmo que calcule e imprima a distância percorrida pelo
# objeto.

# 05 
velociade_inicial = float (input("digite sua velociadade inicial em m/s:"))
aceleracao = float (input("digite a aceleração em m/s:"))
tempo = float (input("digite o tempo de desclocamento (s):"))

distancia = (velociade_inicial * tempo ) + (0.5 * aceleracao *(tempo**2))

print (f"a distância percorrida pelo objeto é de {distancia} metros ")