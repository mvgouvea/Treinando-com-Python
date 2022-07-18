#Tomada de decisões
""" Parte I
print("Instrução if")
a = 10
if(a==10):
    print("O valor de é", a==10)
if(a==11):
    print("Neste caso a mensagem não aparece")
"""
acao = int(input("Digite '1' para sim '2' para não: "))
#caso não converta a variavel, uma forma de descobrir é depurando o arquivo

if(acao==1):
    print("Você disse que sim")
elif(acao==2):
        print("Você disse que não")
elif(acao<1 or acao>2):
    print("Número Inválido: %d" %(acao))
