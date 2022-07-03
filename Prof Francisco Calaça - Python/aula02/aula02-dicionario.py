from traceback import print_exc


dicionario = {}

dicionario["nome"] = "Maria"
dicionario["endereco"] = "Rua 1"

print(type(dicionario))
print(dicionario)

print(dicionario["nome"])
print(dicionario["endereco"])

#Pegando somente o valor informado

dicionario_diferente = {'nome':'Jose', 'endereco': 'Rua 2'}

#Solitando somente o nome
print(dicionario_diferente["nome"])