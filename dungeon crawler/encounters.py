import random
import game
import time

encounterChance = [1,2,3,4,5,6]
randomNumbers = [1,2,3,4,5,6,7,8,9,10]
guessNumber = [1,2,3]

def numberGuessEncounter():
    print("You enter the next room and you encounter a monster")
    time.sleep(3)
    print("To beat the monster you must guess the number the monster is thinking")
    time.sleep(3)
    print("The number will be either 1, 2 or 3")
    time.sleep(3)
    print("What do you guess")
    time.sleep(3)
    playerInput = input()
    if playerInput == random.choice(guessNumber):
        print("you have successfully guess the number and beatened the monster and you are able to continue forward")
        time.sleep(3)
    elif playerInput != random.choice(guessNumber):
        print("You have guessed the wrong number and take damage")
        time.sleep(3)
        global PlayerHP
        game.player.playerHP -= random.choice(randomNumbers)
        print("Your HP Is",game.player.playerHP)

def hangManEncounter():
    print("lorem ipsum")

def encounterSelector():
    if random.choice(encounterChance) >= 4:
        if random.choice(randomNumbers) <= 5:
            numberGuessEncounter()
        else:
            hangManEncounter()
