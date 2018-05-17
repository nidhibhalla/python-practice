from random import randint

def main():
    repeat= True
    print("press enter to roll the dice")
    input()
    while repeat:
        print("you rolled number", randint(1,6))
        print("Do you want to roll again? Y/N")
        repeat = "y" in input()
    print("Thank you for playing")


main()
    
