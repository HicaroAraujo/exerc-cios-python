# “Era uma vez um pequeno vilarejo chamado TechVille, onde os moradores eram grandes
# entusiastas de tecnologia e programação. A vila tinha um grupo de amigos que adoravam resolver
# problemas práticos do dia a dia usando suas habilidades em programação, especialmente em
# Python. Eles se chamavam de "Os Pythonistas de TechVille". Vamos acompanhar as aventuras e
# desafios que eles enfrentaram usando suas habilidades em Python.”

# 2) A Organização da Biblioteca
# A biblioteca de TechVille queria reorganizar seus livros segundo o número de páginas dos livros, tanto em
# ordem crescente quanto decrescente. Os Pythonistas foram chamados para desenvolver um programa que
# recebesse a lista de números de páginas e ordenasse conforme necessário.


# receber uma lista de paginas

paginas = input("digite o número de páginas de cada livro separadas por espaço, por favor:").split()

# trasnformei em valores inteiros 
paginas2 = [int(pagina) for pagina in paginas]

# coloquei a lista em ordem 
ordem = sorted(paginas2)
# inverti a lista ordenada para decrescente
paginas2.sort(reverse=True)

# print(paginas) >>> print de verificação
print(f"Lista em ordem crescente: {ordem}")
print(f" Lista em ordem decrescente: {paginas2}")