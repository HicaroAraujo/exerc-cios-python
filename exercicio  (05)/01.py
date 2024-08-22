# você está desenvolvendo um programa para calcular a corrente elétrica em um cricuito elétrico.O usuário deve informar a resistência e a tensão elétrica do circuito.
#  escreva um algoritimo que calcule e imprima a corrente elétrica do circuito, de acordo com a lei de OHM.


resistencia = int(input("digite a resistência do circuito:"))
tensao = int(input("digite a tensão elétrica do circuito:"))


corrente = resistencia/tensao 

print(f"a corrente elétrica do circuito é {corrente}")



