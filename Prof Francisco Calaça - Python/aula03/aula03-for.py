lista = [1, 2, 3, 4, 5]

for v in lista:
    print(v)
print("------------------------------")

v = int(input("Informe a quantidade de repetições: "))
for i in range(v): #range retorna uma lista
    print(i)
print("------------------------------")

print("A seguir será executado os valores entre dois intervalos, favor digitar")
x = int(input("Informe o primeiro intervalo: "))
z = int(input("Informe o segundo intervalo: "))

for i in range(x, z): #range retorna uma lista
    print(i)
print("------------------------------")