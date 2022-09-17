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
def getTemperatura():
    content = urlopen(req).read()
    content = str(content)
    find = 'max-temp-1">'
    posicao = int(content.index(find) + len(find))
    maxima = content[posicao: posicao + 2]
    maxima = maxima + "º"

    #Temperatura Mínima
    content = urlopen(req).read()
    content = str(content)
    find = 'min-temp-1">'
    posicao = int(content.index(find) + len(find))
    minima = content[posicao: posicao + 2]
    minima = str(minima + "º")
    return [maxima, minima]

temp = getTemperatura()

def getDolar():
    #Cotação Dolar
    content = urlopen(reqDolar).read()
    content = str(content)
    find = '<input type="hidden" value="'
    posicao = int(content.index(find) + len(find))
    dolar = content[ posicao : posicao  + 4]
    return dolar

def getEuro():
    #Cotação Euro
    content = urlopen(reqEuro).read()
    content = str(content)
    find = '<input type="hidden" value="'
    posicao = int(content.index(find) + len(find))
    euro = content[ posicao : posicao  + 4]
    return euro

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
        print("Temperatura Máxima: "+ temp[0])
        print("Temperatura Mínima: "+ temp[1])
    elif escolha == 2:
        print("Dolar hoje: "+ getDolar())
        print("Euro hoje: " + getEuro())
    print("------------------------")
    print("Escolha a opção desejada")
    print("1 - Temperatura atual: ")
    print("2 - Cotação Dolar e Euro hoje: ")
    print("0 - Sair")
    escolha = int(input("Escolha a opção desejada: "))
    print("------------------------")
print("Você escolheu a opção (%i). Obrigado volte sempre "%(escolha))
