# 6) O Concurso de Nomes
# Em um concurso de talentos, os organizadores queriam saber qual era o nome mais longo entre os
# participantes e se todos os nomes tinham a mesma quantidade de caracteres. Os Pythonistas criaram um
# programa para resolver esse problema.

nomes = input("digite uma lista de nomes, seprados por espaços: ").split()
longo = ""
# variavel longo recebe um valor vazio até o proximo comando

for nome in nomes:
    if len(nome) > len(longo):
       longo = nome
print(longo)

if nomes:
    #  para cada nome da lista nomes verificar se é igual ao primeiro numero da lista nomes 
    # O all só vai retornar True se todos forem verdadeiros 
      mesmo_tamanho = all(len(nome) == len(nomes[0]) for nome in nomes)
        
print(f"Todos os nomes têm a mesma quantidade de caracteres? {'Sim' if mesmo_tamanho else 'Não'}")
 




