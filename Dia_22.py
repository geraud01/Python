print ("Advinhe o numero de 0 - 1,000.000")
print ()
print ("Bora começar!")

import random 
tentativas = 2
numero_correto = random.randint (1, 100)

while True:

  numero_advinhado = int(input("Advinhe o numero: "))

  if numero_advinhado > numero_correto:
    print ("O numero correto é menor, tente novamente")
    tentativas = tentativas + 1

  if numero_advinhado < numero_correto:
    print ("O numero correto é maior, tente novamente")      
    tentativas = tentativas + 1

  elif numero_advinhado > numero_correto:
    print ("O numero correto é menor, tente novamente")
    continue
  elif numero_advinhado == numero_correto:  
    print ("Parabens, voce acertou o numero correto!")
    break
else:
  print ("Algo deu errado")
print ("Você acertou o numero em", tentativas, "tentativas")