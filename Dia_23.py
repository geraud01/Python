def login():
  while True:
    usuario = input("Digite o seu usuario: ")
    senha = input("Digite a sua senha: ")
    if usuario == "Geraud" and senha == "1234":
      print("Seja bem-vindo", usuario, "!")
      break
    else:
      print("Usuario ou senha invalidos. Tente novamente!")
      continue
    
print("REPLIT LOGIN SYSTEM")
login()
