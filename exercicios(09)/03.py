# “Era uma vez um pequeno vilarejo chamado TechVille, onde os moradores eram grandes
# entusiastas de tecnologia e programação. A vila tinha um grupo de amigos que adoravam resolver
# problemas práticos do dia a dia usando suas habilidades em programação, especialmente em
# Python. Eles se chamavam de "Os Pythonistas de TechVille". Vamos acompanhar as aventuras e
# desafios que eles enfrentaram usando suas habilidades em Python.”

# 3) Estatísticas do Mercado
# O mercado local queria entender melhor as vendas do mês. Eles pediram aos Pythonistas para criar um
# programa que calculasse a soma, a média, o maior e o menor valor das vendas diárias.

listas = input("digite a lista dos valores de vendas diárias: ").split()

listas = [float(lista) for lista in listas ]

ordem = sorted(listas)

# print de verificação
print(ordem) 

soma = sum(listas)
print(f" A soma  dos valores de venda diárias da lista é: {soma} reais")

# média dos valres da lista 
media = soma / len(listas)
print(f" A média dos valores de venda diárias da lista é: {media} reais ")

# encontrei o maior valor das vendas 
maior= max(listas)
print(f" O maior valor de venda diária da lista é: {maior} reais ")

menor = min(f" O menor valor de venda diária da lista é: {listas} reias")

print(menor)
