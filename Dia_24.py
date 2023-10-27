import random 

print ("Dado infinito")
print ()

lados = int(input("Quantos lados?:"))
jogarJogo = "sim"

def jogarDado(lados):
  print ("Você rolou", random.randint(1,lados))
while jogarJogo == "sim":
    jogarDado(lados)
    jogarJogo = input("Tentar novamente? (sim/não)")
  
print ("Fim do jogo")