#  Calculadora de Consumo de Combustível: Escreva um programa que calcule o consumo médio de
#  combustível de um veículo. O usuário deve informar a quantidade de combustível gasta e a distância
#  total percorrida.

# devo pedir a quantidade de combustivel gasta e a distancia percorrida 
combustivel = int(input("digite a quantidade de combustível gasta em litros:"))
distancia = int(input("digite a distância percorrida pelo veículo (km):"))

media = distancia / combustivel 

print(f"A média de consumo de combustível gasto é de {media} k/l")
# calcular o consumo medio do veiculo 
# printar o resultado para o usuario 

