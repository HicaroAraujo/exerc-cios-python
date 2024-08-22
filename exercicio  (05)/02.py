# Você está desenvolvendo um programa que verifica se uma pessoa pode dirigir ou não. Para isso,
# você precisa solicitar a idade da pessoa e verificar se ela é maior ou igual a 18 anos. Se a idade for
# menor que 18, o programa deve informar que a pessoa não pode dirigir, caso contrário, o programa
# deve informar que a pessoa pode dirigir.


idade = int(input("digite sua idade:"))

if idade >= 18:
    print("você já pode dirigir!")
else:
    print("você ainda não pode dirigir!")