resp = "s"

while resp == "s":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    tot = n1+n2
    print("A soma dos números: %f"%(tot))
    resp = input("Digite s para continuar")
print("Você saiu do programa, volte sempre")