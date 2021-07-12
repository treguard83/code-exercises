from random import randint

x = randint(1,9)*10
guess = -1

print("Guess my tens between 10 and 100: ")

while guess != x:
    guess = int(input("Pick your number: "))
    if guess != x:
        print("WRONG!, try again")
    else:
        print("CORRECT!, you have won the game")
