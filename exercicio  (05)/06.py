# Você está desenvolvendo um programa para classificar triângulos de acordo com as medidas de
# seus lados. O usuário deve informar as medidas dos três lados do triângulo. Escreva um algoritmo
# que determine e imprima se o triângulo é equilátero, isósceles ou escaleno.


lado1 = float(input("digite um lado do triângulo:"))
lado2 = float(input("digite o segundo lado do triângulo:"))
lado3 = float (input("digite o terceiro lado do triângulo:"))

if lado1 == lado2 == lado3 :
    print("esse triângulo é equilátero!")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
     print("esse triângulo é isósciles")
else: 
     print("esse triângulo é escaleno  ")