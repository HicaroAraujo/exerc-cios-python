#  Conversão de Moedas: Crie um programa que converta um valor em reais para dólares. O usuário
#  deve fornecer o valor em reais e a cotação atual do dólar.
reais = float ( input (" digite o valor em reais:"))
cotacao = float(input("digite a cotação atual do dollar :"))

dollar = reais * cotacao

print(f"o valor {reais} reais equivale á {dollar} dollares!")
