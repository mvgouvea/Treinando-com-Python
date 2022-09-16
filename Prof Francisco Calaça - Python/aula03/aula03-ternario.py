#Em Python não é considerado ternario, mas outras linguagens como java, c sim é

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

maior = n1 if n1 > n2 else n2

print("O número maior é : %i" %(maior))