# Hangman game
import time
name = input("Welcome to the game, enter your name: ")
print("Alright {0}, the game is starting...\n".format(name))
print("Hangman.start")
time.sleep(1)

secretWord = "Megaman"
guessedLetters = ''
totalTurns = 10

while totalTurns > 0:
    failed = 0
    for char in secretWord:
        if char in guessedLetters:
            print (char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print("GG")
        break
    guess = input("Choose a letter: ")
    guessedLetters += guess
    if guess not in secretWord:
        totalTurns -= 1
        print("Word not found \nYou have ", +totalTurns, " tries remaining")
    if totalTurns == 0:
        print("Game over, you lose")

