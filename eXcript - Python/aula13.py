num_int = 5
num_dec = 7.3
val_str = "Três formas de concaternar String"

print(val_str)
#Concactenar um valor inteiro com uma String utiliza virgula
print("o valor é:", num_int)
#Dentro da string, se coloca um marcador, utilizando o simbolo do tipo correspondente a variavel %i ou  %f
print("o valor é: %i" %num_int)
print("Tipo real: %f" %num_dec)
#concactena ambos valores string com sinal de adição, em seguida utiliza o cast para conversão.
print("o valor é: "+ str(num_int))