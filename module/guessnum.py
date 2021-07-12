from random import randint

x = randint(11,19)
guess = -1

print("Guess my number between 10 and 20: ")

while guess != x:
    guess = int(input("Pick your number: "))
    if guess != x:
        print("WRONG!, try again")
    else:
        print("CORRECT!, you have won the game")
