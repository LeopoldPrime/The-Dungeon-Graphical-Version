import random
import game

encounterChance = [1,2,3,4,5,6]
randomNumbers = [1,2,3,4,5,6,7,8,9,10]

def numberGuessEncounter():
    print("lorem ipsum")

def hangManEncounter():
    print("lorem ipsum")

def encounterSelector():
    if random.choice(encounterChance) <= 4:
        if random.choice(randomNumbers) <= 5:
            numberGuessEncounter()
        else:
            hangManEncounter()
