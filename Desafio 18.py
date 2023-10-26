print ("Advinhe o numero de 0 - 100")
print ()
print ("Bora começar!")

numero_correto = 42
tentativas = 1

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
print ("Parabens, voce acertou o numero em", tentativas, "tentativas")
    