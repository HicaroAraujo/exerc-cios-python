# Pedro é um estudante de matemática que está desenvolvendo um programa para calcular o volume
#  de uma esfera. Ele sabe que o cálculo pode ser um pouco complicado, mas também é muito
#  em diversas áreas da matemática e da física. Pedro está animado em desenvolver esse
# programa em Python para ajudar outros estudantes a entenderem melhor a fórmula. Escreva um
# algoritmo que ajude Pedro a calcular o volume de uma esfera

# 09
raio = float (input ("digite o raio da esfera:"))
pi = 3.14

volume= (4 * pi * (raio **3 ) ) / 3

print(f"O volume da esfera é de aproximadamente {volume:.2f}")
