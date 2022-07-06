print("Qual a melhor linguagem de programação para quem está começando a programar?")
#Melhor do que dizer qual é a melhor linguagem, é dizer qual o seu perfil?
print("====================== ## ======================")
print("      0 - Sair")
print("      1 - Conhecimento geral das linguagens")
print("      2 - Dominar uma linguagem")
print("====================== ## ======================")
#Lembrando que quando irá comparar um valor é utilizado == dois iguais
escolha = input("Informe sua escolha: ")
#Conversão String para inteiro
escolha = int(escolha)

if escolha == 1:
    print("Estudar mais de uma linguagem ao mesmo??")
    print("É a melhor maneira de conhecer muito e não dominar ABSOLUTAMENTE NADA")
    print("Ou seja, estudando várias linguagens ao mesmo tempo")
    print("Terá um conhecimento geral da linguagens, porém, não conhecerás a fundo NENHUMA")
    print("----------------------------")
    print("**Se o foco é ter conhecimento geral: Estude várias linguagens")
elif escolha == 2:
    #Importância da indentação
    print("É importante estudar uma linguagem")
    print("-----------Conceito----------")
    print("----------Estruturas---------")
    print("----------Construções----------")
if escolha == 0:
    print("Finalizado")
else:
    print("Número não corrrespondente")