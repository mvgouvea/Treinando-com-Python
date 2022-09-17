# import urllib.request
# from urllib.request import Request, urlopen

from urllib.request import Request, urlopen

req = Request(
    url='https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go',
    headers={'User-Agent': 'Mozilla/5.0'}
)

reqDolar = Request(
    url='https://www.melhorcambio.com/dolar-hoje',
    headers={'User-Agent': 'Mozilla/5.0'}
)

reqEuro = Request(
    url='https://www.melhorcambio.com/euro-hoje',
    headers={'User-Agent': 'Mozilla/5.0'}
)


# content = urllib.request.urlopen("req").read()
#Temperatura Máxima
content = urlopen(req).read()
content = str(content)
find = 'max-temp-1">'
posicao = int(content.index(find) + len(find))
maxima = content[posicao: posicao + 2]

#Temperatura Mínima
content = urlopen(req).read()
content = str(content)
find = 'min-temp-1">'
posicao = int(content.index(find) + len(find))
minima = content[posicao: posicao + 2]

#Cotação Dolar
content = urlopen(reqDolar).read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao  + 4]

#Cotação Euro
content = urlopen(reqEuro).read()
#content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
content = str(content)
posicao = int(content.index(find) + len(find))
euro = content[ posicao : posicao  + 4]

print("------------------------")
print("1 - Temperatura atual: ")
print("2 - Cotação Dolar e Euro hoje: ")
print("0 - Sair")
escolha = int(input("Escolha a opção desejada: "))
print("------------------------")
while escolha != 0 :
    if escolha < 0 or escolha > 2:
        print("Opção inválida!! Favor escolha outra")
    elif escolha == 1:
        print("Temperatura Máxima: "+str(maxima),"º")
        print("Temperatura Mínima: "+str(minima),"º")
    elif escolha == 2:
        print("Dolar hoje: "+ dolar)
        print("Euro hoje: " + euro)
    print("------------------------")
    print("Escolha a opção desejada")
    print("1 - Temperatura atual: ")
    print("2 - Cotação Dolar e Euro hoje: ")
    print("0 - Sair")
    escolha = int(input("Escolha a opção desejada: "))
    print("------------------------")
print("Você escolheu a opção( %i )Obrigado volte sempre "%(escolha))
