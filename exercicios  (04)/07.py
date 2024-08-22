# Verificação de senha: Escreva um programa que peça ao usuário uma senha e verifique se
# ela é válida ou não. Considere uma senha válida aquela que possui pelo menos 8
# caracteres, contendo pelo menos uma letra maiúscula e um número. Se a senha for válida,
# exiba a mensagem "Senha válida". Caso contrário, exiba "Senha inválida".

senha = input("digite sua senha:")

if len(senha) < 8:     # len(sequencia) -------->>   quantos elementos(caracteres) a senha contém
  print("senha inválida!")
else: 
   tem_maiuscula = False
   tem_numero = False

   for letra in senha:
    if letra.isupper():  # isupper () ----> verifica se há letras maisuculas
        tem_maiuscula = True
        
for letra in senha:
    if letra.isdigit():   # isdigit() ----> verifica se há numeros na sequencia
        tem_numero = True

    if tem_maiuscula and tem_numero:
     print("senha válida!")
else:
     print("senha inválida!É nescessério ter pelo menos uma letra maiúscula e um número.")



#  for --->  permite iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) e executar um bloco de código para cada elemento dessa sequência.
#  letra ---> varial que recebera cada elemnto da sequência um de cada vez(reprenta os elementos da sequencia)
#  in  ---->  verifica a presença da letra  na senha
#  senha -----> é a sequencia que será interada(verificada)


 

   
