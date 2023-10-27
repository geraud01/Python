print ("Bem vindo ao texte de multiplicação")
print ()

print ("Vamos ver o quanto você sabe sobre multiplicação, Escolha o u numero, e daremos 10 multiplicação para você resolver")

numero_escolhido = int(input("Escolha o numero: "))
print ()

counter = 0
for i in range (1,11):  
  resposta_correta = i*numero_escolhido
  print (i, "x", numero_escolhido)
  resposta = int(input(">"))
  if resposta == resposta_correta:
    print ("Parabéns, você acertou!")
    counter = counter + 1
  else:
    print ("A resposta correta é:", resposta_correta)
    continue
    
  if counter == 10:
    print ("Parabéns, você conseguiu resolver todas as multiplicações 🥳")
  else: 
    print ("Você conseguiu multiplicar", counter, "de um total de 10")