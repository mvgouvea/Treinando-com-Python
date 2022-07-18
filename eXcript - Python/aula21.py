idade = int(input("Informe uma idade:"))
if(idade<=0):
    print("Idade inválida!!",idade)
elif(idade>=150):
        print("Idade inválida!!",idade)
elif(idade > 0 or idade < 150):
    print("Idade válida: %i anos" %(idade))
    if(idade>18):
        print("De maior")
    else:
        print("De menor")