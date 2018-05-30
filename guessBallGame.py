# Guessball project
# Provide a random response, given a user prompt
# Simulate the behavior of the old-school 8-ball game using conditionals, sys import and random import
import sys
import random as r

run = True
while run:
    query = input("What is your query troubled soul? (Press enter to exit) ")
    result = r.randint(1,8)
    if query == "":
        sys.exit()
    elif result == 1:
        print("Perhaps ...")
    elif result == 2:
        print("Yes!")
    elif result == 3:
        print("Of course")
    elif result == 4:
        print("Impossible!")
    elif result == 5:
        print("Kind of? Maybe you should ask.")
    elif result == 6:
        print("Nope!")
    elif result == 7:
        print("Go for it")
    else:
        print("Ask a friend and make it their problem!")
