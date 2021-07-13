from random import randint
import newbies

x = randint(1,9)*10
guess = -1

newbies.printplus(1)

while guess != x:
    guess = int(input("Pick your number: "))
    if guess != x:
        print("WRONG!, try again")
    else:
        print("CORRECT!, you have won the game")
