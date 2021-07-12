from random import randint

x = randint(0,5)
guess = "Z"
vowls = ('A','E','I','O','U')

print("Guess my Vowl: ")

while guess.capitalize() != vowls[x]:
    guess = input("Pick your Vowl: ")
    if guess.capitalize() != vowls[x]:
        print("WRONG!, try again")
    else:
        print("CORRECT!, you have won the game")
