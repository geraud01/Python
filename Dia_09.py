myGeneration = int(input("What generation are you a part of?"))
if myGeneration >= 1925 and myGeneration <= 1945:
  print("Traditionalists")
elif myGeneration >= 1947 and myGeneration <= 1964:
  print("Baby Boomers")
elif myGeneration >= 1965 and myGeneration <= 1981:
  print("Generation X")
elif myGeneration >= 1982 and myGeneration <= 1995:
  print("Millennials")
elif myGeneration >= 1996 and myGeneration <= 2015:
  print("Generation Z")
elif myGeneration >= 2016 and myGeneration <= 2025:
  print("Generation Alpha") 
else: 
  print ("try again")