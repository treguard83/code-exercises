from random import randint

x = randint(0,4)
guess = "Z"
compasspoint = ('N','S','E','W')

print("Guess my Compass Point: ")

while guess.capitalize() != compasspoint[x]:
    guess = input("Pick your compass point from N,S,E,W: ")
    if guess.capitalize() != compasspoint[x]:
        print("WRONG!, try again")
    else:
        print("CORRECT!, you have won the game")
