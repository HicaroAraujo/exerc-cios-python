# João é um médico que trabalha em uma clínica especializada em saúde preventiva. Ele está
# desenvolvendo um programa para calcular o IMC (Índice de Massa Corporal) de seus pacientes. O
# IMC é uma medida que relaciona o peso e a altura de uma pessoa e é utilizada para verificar se ela
# está com o peso ideal. João sabe que, para calcular o IMC, ele precisa da altura e do peso do
# paciente. Escreva um algoritmo em Python que ajude João a calcular o IMC de seus pacientes.

# 07
altura = float(input("digite sua altura:"))
peso = float(input("digite seu peso:"))

imc = peso / altura**2

print(f"O seu índice de massa corporal é {imc}")


