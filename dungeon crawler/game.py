import random
import shop
import rooms
import paths
import time
import encounters 

class player:
    playerHP = 100
    playerCurrency = 0
    healthPotionsCount = 0
    mysticalWeapon = 0
    previousPath = 0
    previousRoomPrinted = 0

randomNumber = [1,2,3,4,5,6,7,8,9,10]

def startingText():
    print(" ")
    print("You're a young barbarian wondering around in your village,")
    time.sleep(3)
    print("When you hear about a mystical weapon hidden deep in a cave,")
    time.sleep(3)
    print("So you decide to venture into the cave to find the mystical weapon")
    time.sleep(3)
    print(" ")

def mainMenu():
    print("==========================")
    print("|                        |")
    print("|      The Dungeon       |")
    print("|                        |")
    print("| Press Start When Ready |")
    print("|                        |")
    print("==========================")
    print(" ")

def healingShrine():
    guessNumber = [1,2]
    if random.choice(randomNumber) >= 6:
        print('You encounter a healing shrint you if you guess the right number you restore some of your hp')
        print('Guess the number it can be 1 and 2')
        playerInput = input()
        if playerInput == random.choice(guessNumber):
            print("You guess correctly the shrine glows green and it heals you")
            player.playerHP += random.choice(randomNumber)
            print("Your HP is now", player.playerHP)
        else:
            print("You guess the wrong number and the shrine crumbles")

mainMenu()
playerInput = input()

if playerInput == "start":
    startingText()
    rooms.startingRooms()

while player.mysticalWeapon < 1:
    rooms.roomSelector()
    paths.pathSelector()
    encounters.encounterSelector()
    healingShrine()