# Project 1 of course:
# Input a number from (1-5)
# Generate random number
# Compare if the number is correct or incorrect

import random
randNum = random.randint(1,5)
usrInput = int(input("Input a number between 1 and 5: "))

if randNum == usrInput:
    print("You guessed correct")
else:
    print ("You guessed wrong")
