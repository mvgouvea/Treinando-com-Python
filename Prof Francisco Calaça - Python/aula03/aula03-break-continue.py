#break: Sai do laço de repetição for ou instrução while
x = 1
y = 10
z = 8
u = 3
for v in range(x, y):
    if(v == z):
        print("Sair forçado, o valor é: " +str(v))
        break
    if(v == u):
        print("Apenas um continue: " +str(v))
        continue
        #print("Isto não será impresso") #mesmo sem comentário
    print("Valor: " +str(v))
print("----------Fim----------")
#continue: pula para próxima iteração