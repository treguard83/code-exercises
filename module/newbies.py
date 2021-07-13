import random

def printplus(x):
    x2 = ("Guess my number between 10 and 20: ","Guess my 10s between 10 and 100: ","Guess my number between 1 and 10: ", "Guess my number between 0 and 1000: ","Guess my Compass Point: ","Guess my Vowel: ")
    print(x2[x])

def numpick(x):
    guess = -1
    while guess != x:
       guess = int(input("Pick your number: "))
       if guess != x:
        print("WRONG!, try again")
       else:
        print("CORRECT!, you have won the game")

def numpickhilow():
    x = randint(1,999)
    guess = -1
    while guess != x:
       guess = int(input("Pick your number: "))
       if guess < x:
        print("Too low, try again")
       elif guess > x:
        print("Too high, try again")
       else:
        print("CORRECT!, you have won the game")

def guesscompass():
    x = randint(0,4)
    guess = "Z"
    compasspoint = ('N','S','E','W')

    while guess.capitalize() != compasspoint[x]:
       guess = input("Pick your compass point from N,S,E,W: ")
       if guess.capitalize() != compasspoint[x]:
        print("WRONG!, try again")
       else:
        print("CORRECT!, you have won the game")

def guessvowels():
    x = randint(0,5)
    guess = "Z"
    vowels = ('A','E','I','O','U')

    while guess.capitalize() != vowels[x]:
      guess = input("Pick your Vowel: ")
      if guess.capitalize() != vowels[x]:
        print("WRONG!, try again")
      else:
        print("CORRECT!, you have won the game")

def guessdecade():
    x = random.randrange(1900,2021,10) 
    guess = -1 
    while guess != x:
       guess = int(input("Pick your decade: "))
       if guess < x:
        print("Too low, try again")
       elif guess > x:
        print("Too high, try again")
       else:
        print("CORRECT!, you have won the game")