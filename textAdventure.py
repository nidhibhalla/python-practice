# move through rooms based on input, get description of each room
#establish the directions in which user can move
#a way to track how far user has moved and print description
#set limits for how far user can move
#create walls, around room that could tell the user you cant move further
#strings, varialble, i/o, if/else, print, list, integers
#textbasedadventure game

def textadventure():

    print("Welcome to the adventure world, there are two colorful room with different entities")
    room = input("enter the room you wants to go in? 'room1', 'room2'")

    if "room1" in room:
        room1()
    elif "room2" in room:
        room2()
    else:
        print("you have not entered anywhere")


def room1():
    print("welcome to room1, this is green color room.. where you can move right or left, you will find different entities")
    dir = input("which direction you wants to go? left or right")
    left = 0
    right = 0
    if "left" in dir:
        left=left+1
        print("you have moved a step to left, there is one bread stick, do you want to try it? y/n")
        y_n = input()
        if "y" in y_n:
            sticks=['fish','cream', 'chips', 'salad']
            print("you have got so many things with bread sticks, as below:")
            for stick in sticks:
                print(stick)
            print("now you are eligble for room2")
            room2()
        else:
            print("you have selected 'No', so you are not eligble for room2 and csn exit the game")
    if "right" in dir:
        right = right+1
        print("you have moved a step to right, there is no where to go and you can exit the game")
        
def room2():
    print("welcome to room2, this is white color room .. where you can move north or south, and find treasures")
    dir = input("which direction you wants to go? south or north")
    north = 0
    south = 0
    if "north" in dir:
        north=north+1
        print("you have moved a step to north, there is one small box of treasure, do you want to take it? y/n")
        y_n = input()
        if "y" in y_n:
            gems=['ruby','diamonds', 'emerald', 'garnet']
            print("you have got so many gems, as below:")
            for gem in gems:
                print(gem)
            print("do you want to move different direction? y/n")
            dir = input()
            if'y' in dir:
                print("you have got enough!, you can exit the game")
            if'n' in dir:
                print("Hey!, you have got more treasure, you won. Game is finished")
            
    if "south" in dir:
        south = south+1
        print("you have moved a step south and you can exit the game")


textadventure()
