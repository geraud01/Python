from getpass import getpass as input

print ("Pedra, 🪨 Papel 📄 e Tesoura ✂️ ")
print ()
print ("Escolha o seu movimento (Pedra, Papel ou Tesoura)")
print ()

play1Move = input("Player 1: ")
print ()
play2Move = input("Player 2: ")
print ()

if player1move == "pedra":
  if player2move == "pedra":
    print ("Vocês escolheram pedra, empate!")
  elif player2move == "papel":
    print ("Player 2 ganhou!")
  elif player2move == "tesoura":
    print ("Player 1 ganhou!")  
  else:
    print ("Jogada inválida!")  
elif player1move == "papel":
  if player2move == "pedra":
    print ("Player 1 ganhou!")
  elif player2move == "papel":
    print ("Vocês escolheram papel, empate!")
  elif player2move == "tesoura":
    print ("Player 2 ganhou!")  
  else:
    print ("Jogada inválida!")  
elif player1move == "tesoura":
  if player2move == "pedra":
    print ("Player 2 ganhou!")
  elif player2move == "papel":
    print ("Player 1 ganhou!")  
  elif player2move == "tesoura":
    print ("Vocês escolheram tesoura, empate!")  
  else:
    print ("Jogada inválida!")  