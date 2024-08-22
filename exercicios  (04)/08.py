# Cálculo de imposto: Escreva um programa que leia o salário de um funcionário e calcule o
#valor do imposto a ser pago, considerando as seguintes faixas salariais: até R$ 1.000,00,
#isento de imposto; de R$ 1.000,00 a R$ 2.000,00, 10% de imposto; acima de R$ 2.000,00,
#20% de imposto.

salario = float(input("digite seu sálario:"))

taxa_imposto1 = 0 # insento de impostos
taxa_imposto2 = 0.10 # 10 % de imposto
taxa_imposto3 = 0.20 # 20% de imposto

if salario < 1000:
    imposto = salario * taxa_imposto1
    
elif salario >= 1000 and salario <= 2000:
    imposto = salario * taxa_imposto2

else:
    imposto = salario * taxa_imposto3

# para printar o valor do imposto em REAIS é nescessário declarar variáveis.


if salario < 1000:
 print(f"você é insento de impostos!")
 
elif salario >= 1000 and salario <= 2000:
 print(f"Você irá pagar {imposto} reias de imposto!") 

else:
   print(f"você irá pagar {imposto:.2f} reais de imposto!")
