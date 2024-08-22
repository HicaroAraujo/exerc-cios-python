# Uma loja de roupas está com uma promoção de 20% de desconto em todos os produtos.
# Uma blusa custava R$ 80, quanto ela custará agora?

promocao = 20
valor = 80 

#             80 \ / 100
#  desconto = x  / \  20

desconto = (valor * promocao ) / 100

valorfinal = valor - desconto

print(f"Com o desconto a blusa custará {valorfinal}")