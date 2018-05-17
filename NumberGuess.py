import random

numberofguess = 0
number = random.randint(1, 10)

name = input("Please enter your name ")
print("Hello %s, guess a whole number between 1 to 10" % name)

while numberofguess <3:
    guess= int(input("Take a guess  "))
    numberofguess+=1
    guessleft = 3- numberofguess

    if guess<number:
        print("number is too low")
        
    elif guess>number:
        print("number is too high")

    elif guess==number:
        print("you are correct")
        print("Number of guesses are %d" % guessleft)
        break
    else:
        print("invalid number")
    print("you have %d chances left" % guessleft)

print("Thank you for playing!")
