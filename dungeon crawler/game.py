import paths
import encounters
import shop
import rooms
import time
import random

class player:
    playerHP = 100
    playerCurrency = 0
    healthPotionsCount = 0
    mysticalWeapon = 0
    previousPath = 0
    previousRoomPrinted = 0

def startingText():
    print("You're a young barbarian wondering around in your village,")
    time.sleep(2)
    print("When you hear about a mystical weapon hidden deep in a cave,")
    time.sleep(2)
    print("So you decide to venture into the cave to find the mystical weapon")
    time.sleep(2)

def mainMenu():
    print("==========================")
    print("|                        |")
    print("|      The Dungeon       |")
    print("|                        |")
    print("| Press Start When Ready |")
    print("|                        |")
    print("==========================")

startingText()
mainMenu()
playerInput = input()

if playerInput == "start":
    rooms.startingRooms()