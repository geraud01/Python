print("\033[035mBem vindo ao gerador de numeros")
print()

x = int(input("\033[0mQual numero você deseja começar? "))
y = int(input("Qual numero você deseja terminar?"))
z = int(input("Quantos devo adicionar de cada vez? "))

for i in range(x, y, z):
  print(i)
