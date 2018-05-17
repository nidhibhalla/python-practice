import random

def main():
        rand_num = random.randint(1, 10)
        name = input("please enter your name ")
        print("Hello", name)
        while True:
         number = int(input("Guess a number between 1 to 10 "))
         if number == rand_num:
            print("you are correct")
         elif  number<rand_num:
            print("Too low")
         else: print("Too high")

         y_n =input("do you want to try again? y or n  ")
         if y_n =='n': break
         else: continue
    

main()
