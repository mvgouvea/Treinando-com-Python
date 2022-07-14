#Modulo de Divisão
from lib2to3.pytree import convert


print("O resto da divisão é intentificado com %")
print(7%2)

print("Número exato")
print(900%100==0)

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1/num2
resto = num1/num2
print()
print("-----Modelo 1-----")
print("Neste modelo observe vem várias casas decimais")
print(num1, "divido por", num2, "é igual a:", divisao)
print("O resto entre", num1, "e", num2, "é igual a:", resto)
print()
print("-----Modelo 2-----")
print("Neste modelo foi fixado que será apresentado 3 casas decimais após a virgula")
print("%.3f dividio por %.3f é igual a: %.3f" %(num1, num2, divisao))
print("O resto entre %.3f e %.3f é igual %.3f" %(num1, num2, resto))
