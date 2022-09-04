import random

def forwardRoomOne():
    print("        | |       ")
    print("        | |       ")
    print("        |  =======")
    print("        |X =======")
    print("        | |       ")
    print("        | |       ")
def forwardRoomTwo():
    print("                  ")
    print("                  ")
    print("==================")
    print("======== X =======")
    print("        | |       ")
    print("        | |       ")

def forwardRoomThree():
    print("        | |       ")
    print("        | |       ")
    print("========  |       ")
    print("======== X|       ")
    print("        | |       ")
    print("        | |       ")

def forwardRoomFour():
    print("                  ")
    print("                  ")
    print("==========        ")
    print("======== X|       ")
    print("        | |       ")
    print("        | |       ")

def startingRoom():
    print("        | |       ")
    print("        | |       ")
    print("========   =======")
    print("======== X =======")
    print("        | |       ")
    print("        | |       ")

allRoomsForward = [forwardRoomOne(),forwardRoomTwo(),forwardRoomThree(),forwardRoomFour(),]
#allRoomsRight = [rightRoomOne(),rightRoomTwo(),rightRoomThree(),rightRoomFour(),]
#allRoomsLeft = [leftRoomOne(),leftRoomTwo(),leftRoomThree(),leftRoomFour(),]

randomRoomForward = random.choice(allRoomsForward)
#randomRoomRight = random.choice(allRoomsRight)
#randomRoomLeft = random.choice(allRoomsLeft)