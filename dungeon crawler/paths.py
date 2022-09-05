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