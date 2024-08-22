nomes = input("digite uma lista de nomes, separadas por espaço, por gentileza: ").split()

maior = max(nomes, key=len)


print(maior)