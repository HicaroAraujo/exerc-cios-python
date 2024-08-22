#Faça um algoritmo que calcule a distância percorrida por um veículo com base
#  em sua velocidade e tempo de percurso informados pelo usuário e imprima o resultado.

velocidade = int (input("digite a velocidade em km/h"))
tempo = int (input("digite o tempo em horas"))

distancia = velocidade * tempo 

print (f" a distancia percorrida pelo veiculo foi de {distancia}km")
