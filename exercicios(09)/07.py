nomes = input("digite uma lista de nomes, separados por espaço, por favor: ").split()

# para cada nome na lista de nomes verificar se é igual o primeiro nome da lista
mesmo = all(len(nome) == len(nomes[0]) for nome in nomes)

# se a variavel mesmo for igual a true print sim caso contrario print não
print(f"todos os nomes tem a mesma quantidade de caracteres? {'resposta: Sim' if mesmo else 'resposta: Não'}")