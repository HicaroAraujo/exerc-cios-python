#  Cálculo de desconto: Escreva um programa que leia o valor de um produto e calcule o valor
#  com desconto de 10%. Se o valor do produto for maior que R$ 50,00, aplique um desconto
#  adicional de 5%. Exiba o valor final com desconto.

valorproduto = float(input("digite o valor do produto:"))
desconto = 0.10            # valor de 10%
descontoadicional = 0.05   # valor de 15% 


if valorproduto > 50:
    valor_desconto = valorproduto * (desconto + descontoadicional )

else:
  valor_desconto = valorproduto * desconto

valorfinal = valorproduto - valor_desconto

print (f"o valor de desconto é de R$ {valor_desconto:.2f}")

print(f"o valor do produto com desconto fica R${valorfinal}")

