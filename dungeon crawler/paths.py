import game

pathsTwo = "Left or Right"
pathsThree = "Forward or Right"
pathsFour = "Forward or Left"

forwardOutput = "You move forward progressing deeper into the cave"
rightOutput = "You turn right progressing deeper into the cave"
leftOutput = "You turn left progressing deeper into the cave"

def pathSelector():
    if game.player.previousRoomPrinted == 11:
        print(pathsThree)
        playerInput = input()
        if playerInput == "forward":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 1
        elif playerInput == "right":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 3
    elif game.player.previousRoomPrinted == 12:
        print(pathsTwo)
        playerInput = input()
        if playerInput == "left":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 2
        elif playerInput == "right":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 3
    elif game.player.previousRoomPrinted == 13:
        print(pathsFour)
        playerInput = input()
        if playerInput == "forward":
            print(forwardOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 1
        elif playerInput == "left":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 2
    elif game.player.previousRoomPrinted == 21:
        print(pathsThree)
        playerInput = input()
        if playerInput == "forward":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 1
        elif playerInput == "right":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 3
    elif game.player.previousRoomPrinted == 22:
        print(pathsFour)
        playerInput = input()
        if playerInput == "forward":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 1
        elif playerInput == "left":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 2
    elif game.player.previousRoomPrinted == 23:
        print(pathsTwo)
        playerInput = input()
        if playerInput == "right":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 3
        elif playerInput == "left":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 2
    elif game.player.previousRoomPrinted == 31:
        print(pathsThree)
        playerInput = input()
        if playerInput == "forward":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 1
        elif playerInput == "right":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 3
    elif game.player.previousRoomPrinted == 32:
        print(pathsFour)
        playerInput = input()
        if playerInput == "right":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 3
        elif playerInput == "left":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 2
    elif game.player.previousRoomPrinted == 33:
        print(pathsFour)
        playerInput = input()
        if playerInput == "forward":
            print(rightOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 1
        elif playerInput == "left":
            print(leftOutput)
            game.player.previousPath -= game.player.previousPath
            game.player.previousPath += 2

