#Faça um algoritmo que calcule o desconto de um produto com base em sua porcentagem de desconto e imprima o preço final.


valororiginal = float(input("digite o valor original:"))
desconto = float( input("digite o valor de descoto:"))

valorfinal = (valororiginal /100 ) * (100 - desconto)


print (f"o precço final fica:{valorfinal:.2f}")


#  usei regra de tres 

# (valorOriginal /100 ) = 1 % do valor do produto  e (100 - desconto) é = porcentagem de desconto do produto
#  1 % valor do produto x porcentagem do produto = valor final do produto

