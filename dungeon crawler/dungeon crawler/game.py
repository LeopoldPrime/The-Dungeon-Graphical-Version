import rooms
import paths
import encounters
import shop
import time
import random

class player:
    playerHP = 100
    playerCurrency = 0
    healthPotionsCount = 0
    mysticalWeapon = "No"

def startingText():
    print("You're a young barbarian wondering around in your village,")
    time.sleep(1)
    print("When you hear about a mystical weapon hidden deep in a cave,")
    time.sleep(1)
    print("So you decide to venture into the cave to find the mystical weapon")
    time.sleep(1)

def mainMenu():
    print("==========================")
    print("|                        |")
    print("|      The Dungeon       |")
    print("|                        |")
    print("| Press Start When Ready |")
    print("|                        |")
    print("==========================")
