#  Controle de Gastos Pessoais: Escreva um programa para ajudar as pessoas a controlar seus gastos
#  mensais. O programa deve permitir que o usuário registre seus gastos em diferentes categorias (por
#  exemplo, alimentação, transporte, moradia) e calcule o total gasto em cada categoria e o total geral.

while True:
    print("""
          MENU:
          1- Adicionar despesa de Alimentação:
          2- Adicionar Despesa de Transporte:
          3- Adicionar despesa de Moradia:
          4- Exibir Total:
          5- Zerar contadores
          6- SAIR""")
    
    opc = int(input("Digite a opção desejada:"))
    
    if opc == 1:
        print("Despesa com Alimentação:")
        gasto = float(input("Digite o valor gasto:"))
        alimentacao += gasto
        total += gasto
    elif opc == 2:
        print("Despesa com Transporte:")
        gasto = float(input("Digite o valor gasto:"))
        transporte += gasto
        total += gasto
    elif opc == 3:
        
        print("Despesa com Moradia:")
        gasto = float(input("Digite o valor gasto:"))
        moradia += gasto
        total += gasto
    elif opc == 4:
        print(f"""
          Totalizadores:
          1- Despesa de Alimentação R$:{alimentacao:.2f}
          2- Despesa de Transporte R$:{transporte:.2f}
          3- Despesa de Moradia R$:{moradia:.2f}
          4- Total  Geral R$:{total:.2f}
          """)
    elif opc == 5:
        alimentacao = 0
        transporte = 0
        moradia = 0
        total = 0
    elif opc == 6:
        break
    else:
        print("Escolha uma opção válida!")