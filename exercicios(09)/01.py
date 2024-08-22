# “Era uma vez um pequeno vilarejo chamado TechVille, onde os moradores eram grandes
# entusiastas de tecnologia e programação. A vila tinha um grupo de amigos que adoravam resolver
# problemas práticos do dia a dia usando suas habilidades em programação, especialmente em
# Python. Eles se chamavam de "Os Pythonistas de TechVille". Vamos acompanhar as aventuras e
# desafios que eles enfrentaram usando suas habilidades em Python.”

# 1) A Feira de Números
# Durante a feira anual de TechVille, os organizadores quiseram saber a média dos números pares dos
# ingressos vendidos. Eles pediram aos Pythonistas para criar um programa que pudesse receber a lista de
# todos os números dos ingressos e calcular essa média.

# pedri numero
numeros = input("digite uma lista de numeros separados por espaços").split()

# transformei em uma lista de valores inteiros 
numero1 = [int(numero) for numero in numeros]
lista_pares= []

for numero3 in numero1:
     if numero3 % 2 == 0:
      lista_pares.append(numero3) 

      media = sum(lista_pares) / len(lista_pares)

print(f"lista inteira{numeros}")
print(f"listas de numeros pares  : {lista_pares}")    
print (f"E a média desses numeros paraes fica: {media}")
    
  
