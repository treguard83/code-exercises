from random import randint

x = randint(1,9)
guess = -1

print("Guess my number between 1 and 10: ")

while guess != x:
    guess = int(input("Pick your number: "))
    if guess != x:
        print("WRONG!, try again")
    else:
        print("CORRECT!, you have wont the game")
