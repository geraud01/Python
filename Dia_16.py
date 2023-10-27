print ("Seja bem-vindo ao jogo 'Qual é a musica'")
counter = 1
while True:
  lyrics = input("Quem não tem teto de vidro, que ______ a primeira pedra ")
  if lyrics == "atire" or lyrics == "Atire":
    print ("Parabéns, você acertou a primeira letra da música")
  else:
    print ("Você errou a primeira letra da música")
    counter += 1
    if lyrics == "atire" or lyrics == "Atire":
      break
  print("Obrigado por jogar! <3")

  print("Você acertou em", counter, "tentativas")