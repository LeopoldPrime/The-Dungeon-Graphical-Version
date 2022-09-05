import random
import game
import paths

randomNumbers = [1,2,3]

def forwardRoomOne():
    print("        | |       ")
    print("        | |       ")
    print("        |  =======")
    print("        |         ")
    print("        |X =======")
    print("        | |       ")
    print("        | |       ")

def forwardRoomTwo():
    print("                  ")
    print("                  ")
    print("==================")
    print("                  ")
    print("======== X =======")
    print("        | |       ")
    print("        | |       ")

def forwardRoomThree():
    print("        | |       ")
    print("        | |       ")
    print("========  |       ")
    print("          |       ")
    print("======== X|       ")
    print("        | |       ")
    print("        | |       ")

def startingRoom():
    print("        | |       ")
    print("        | |       ")
    print("========   =======")
    print("                  ")
    print("======== X =======")
    print("        | |       ")
    print("        | |       ")

def leftRoomOne():
    print("        | |       ")
    print("        | |       ")
    print("========   =======")
    print("           X      ")
    print("==================")
    print("                  ")
    print("                  ")

def leftRoomTwo():
    print("                  ")
    print("                  ")
    print("==================")
    print("           X      ")
    print("========   =======")
    print("        | |       ")
    print("        | |       ")

def leftRoomThree():
    print("        | |       ")
    print("        | |       ")
    print("        |  =======")
    print("        |  X      ")
    print("        |  =======")
    print("        | |       ")
    print("        | |       ")

def rightRoomOne():
    print("                  ")
    print("                  ")
    print("==================")
    print("       x          ")
    print("========   =======")
    print("        | |       ")
    print("        | |       ")

def rightRoomTwo():
    print("        | |       ")
    print("        | |       ")
    print("========  |       ")
    print("       x  |       ")
    print("========  |       ")
    print("        | |       ")
    print("        | |       ")

def rightRoomThree():
    print("        | |       ")
    print("        | |       ")
    print("========   =======")
    print("       x          ")
    print("==================")
    print("                  ")
    print("                  ")

def roomSelector():
    if game.player.previousPath == 1:
        roomNumber = random.choice(randomNumbers)
        if roomNumber == 1:
            forwardRoomOne()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 11
        elif roomNumber == 2:
            forwardRoomTwo()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 12
        elif roomNumber == 3:
            forwardRoomThree()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 13
    elif game.player.previousPath == 2:
        roomNumber = random.choice(randomNumbers)
        if roomNumber == 1:
            leftRoomOne()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 21
        elif roomNumber == 2:
            leftRoomTwo()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 22
        elif roomNumber == 3:
            leftRoomThree()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 23
    elif game.player.previousPath == 3:
        roomNumber = random.choice(randomNumbers)
        if roomNumber == 1:
            rightRoomOne()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 31
        elif roomNumber == 2:
            rightRoomTwo()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 32
        elif roomNumber == 3:
            rightRoomThree()
            game.player.previousRoomPrinted -= game.player.previousRoomPrinted
            game.player.previousRoomPrinted += 33

def startingRooms():
    startingRoom()
    print("Forward, Left or Right")
    playerInput = input()
    if playerInput == "forward":
        forwardRoomOne()
        game.player.previousRoomPrinted -= game.player.previousRoomPrinted
        game.player.previousRoomPrinted += 11
    elif playerInput == "left":
        leftRoomOne()
        game.player.previousRoomPrinted -= game.player.previousRoomPrinted
        game.player.previousRoomPrinted += 21
    elif playerInput == "right":
        rightRoomOne()
        game.player.previousRoomPrinted -= game.player.previousRoomPrinted
        game.player.previousRoomPrinted += 31
