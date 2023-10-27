exit = "no"

while exit == "no":
    animal_sound = input("What animal do you want to hear?")

    if animal_sound == "cow":
        print(" 🐮moo")
    elif animal_sound == "pig":
        print(" oink")
    elif animal_sound == "dog":
        print(" woof")
    elif animal_sound == "cat":
        print(" meow")
    elif animal_sound == "horse":
        print(" neigh")
    elif animal_sound == "duck":
        print(" quack")
    else:
        print("Sorry, I don't know that animal sounds.Please, try again")
             
    exit = input("Do you want to exit? (yes/no):")