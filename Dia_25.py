# 1 - Create a subroutine that rolls a dice of any size and returns that number.
# 2 - Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
# 3 -Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
# 4 -Print out the character's health stats.
# 5 -Add a loop to give the user the option to generate health stats for another character.

import random

def jogar_dados(lados):
    resultado = random.randint(1, lados)
    return resultado
  
def jogar_6_e_8():  
  dados_de_seis_lados = jogar_dados(6)
  dados_de_oito_lados = jogar_dados(8)
  saude = dados_de_seis_lados  * dados_de_oito_lados
  return saude

print ("⚔️ Character Stats Generator ")
print ()

temUmPersonagem = "sim"

while temUmPersonagem == "sim":
  personagem = input ("Nome do seu guerreiro: ")
  saude = str (jogar_6_e_8())
  print ("A saude dele é", saude, "hp")
  temUmPersonagem = input ("Deseja gerar stats de outro personagem? (sim/não)")