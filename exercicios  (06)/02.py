# Decomposição de Valor em Notas e Moedas: Desenvolver um programa em Python que receba um
# valor em reais do usuário e decomponha esse valor no menor número possível de notas de R$ 100, R$
# 50, R$ 20, R$ 10, R$ 5, R$ 2 e moedas de R$ 1.
# Exemplo de saída:
# Digite o valor em reais: 489
# Notas de R$100: 4
# Notas de R$50: 0
# Notas de R$20: 1
# Notas de R$10: 1
# Notas de R$5: 1
# Notas de R$2: 2
# Moedas de R$1: 0

valor = int(input("digite o valor:"))

cem = valor // 100
print(f"Notas de R$100 = {cem}")
resto = valor % 100  # 89

cinquenta = resto // 50 
print(f"Notas de R$50 = {cinquenta}")
resto = resto % 50 # 39

vinte = resto // 20 
print(f"Notas de R$20 = {vinte}")
resto = resto % 20 # 19

dez = resto // 10 
print(f"Notas de R$10 = {dez}")
resto = resto % 10 # 9

cinco = resto // 5
print(f"Notas de R$5 = {cinco}")
resto = resto % 5 # 4

dois = resto // 2
print(f"Notas de R$2 = {dois}")
resto = resto % 2 # 0

um = resto // 1
print(f"Moeda de R$1 = {um}")
resto = resto // 1 # 0

