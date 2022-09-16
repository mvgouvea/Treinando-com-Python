idade = int(input("Digite a idade: "))

if idade < 16 :
    print("Não pode votar")
elif idade >= 16 and idade <18 or idade > 70:
    print("Pode votar (Não é Obrigatório)")
else:
    print("Pode Votar (É obrigatório)")
