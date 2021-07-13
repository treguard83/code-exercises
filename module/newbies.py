def printplus(x):
    x2 = ("Guess my number between 10 and 20: ","Guess my 10s between 10 and 100: ")
    print(x2[x])

def numpick(x):
    guess = -1
    while guess != x:
       guess = int(input("Pick your number: "))
       if guess != x:
        print("WRONG!, try again")
       else:
        print("CORRECT!, you have won the game")