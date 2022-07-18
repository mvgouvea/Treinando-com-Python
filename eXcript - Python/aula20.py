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
if(acao==1):
    print("Você disse que sim")
else:
    if(acao==2):
        print("Você disse que não")
    else:
        print("Você não disse nenhum dos números acima")
