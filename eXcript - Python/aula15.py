#informar o usuário a digitar e armazenar na memória
login = input("Login: ")
senha = input("Senha: ")
#O uso do percentual funciona como marcador, desta maneira vai em ordem de chegada
print("O usuário informado foi: %s, e a senha digitada foi: %s" %(login, senha))
#é necessário utilizar o %(variaveis em sequencia)