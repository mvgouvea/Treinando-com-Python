#Destrinchando String
texto = "Um texto qualquer"
nome = "Marcos"
posicao = texto.index("qual") #busca determinado texto dentro da string
resultPosicao = len(texto) # calcula o tamanho
a = str(len("marcos")) #calcula o tamanho do texto, 5 posições
print(posicao)
print(resultPosicao)
print("Quantidade de caracteres da palavra %s: %s" %(nome, a))

#Sub String é entre cochetes
qua = 5
posicao = texto.index("t")
resultado = texto[posicao : posicao + qua]
print("Resultado de substring: %s" %(resultado))