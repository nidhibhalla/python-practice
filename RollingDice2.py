import random

def main():
    min=1
    max=6
    roll_again="yes"

    while roll_again=="yes":
        print("Rolling the dices")
        number = random.randint(min, max)
        print(" number is %d" % number)
        print("Roll the dice? yes or no")
        yes_no = input()
        roll_again=yes_no.lower()
    print("Thank you for playing!")


main()
