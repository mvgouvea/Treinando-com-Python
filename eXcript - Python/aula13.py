num_int = 5
num_dec = 7.3591
val_str = "qualquer texto"

print("Três formas de concaternar String")
#Concactenar um valor inteiro com uma String utiliza virgula
print("o valor é:", num_int)
#Dentro da string, se coloca um marcador, utilizando o simbolo do tipo correspondente a variavel %i ou  %f
print("o valor é: %i" %num_int)
#para contrar a quantidade de casas decimais, basta colocar %. e a quantidade seguido do f
print("Tipo real: %.3f" %num_dec)
#concactena ambos valores string com sinal de adição, em seguida utiliza o cast para conversão.
print("o valor é: "+ str(num_int))
#para concactena é necessário ambos ser do mesmo tipo
print("#-------------------#")
print("Concactenando strings", val_str)
print("Concactenando strings %s" %val_str)
print("Concactenando strings "+ val_str)