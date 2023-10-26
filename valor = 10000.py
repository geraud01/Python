valor = 10000
juros = 0.20

for i in range(10):
  valor+= (valor*juros)
  print ("Ano", i+1, "é de", round(valor))