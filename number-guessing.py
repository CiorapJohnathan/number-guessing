import numpy as np
print("Welcome to the guess the number")
print("The rules are simple")
print("Guess a number between 1-100, u have 7 attempts")
while True:
    attempts=0
    nrPC=np.random.randint(1,101)
    while attempts<7:
        guess=int(input("Choose a number "))
        while True:
            if guess < 1 and guess > 100:
                print("Pick a number between 1-100")
                guess=int(input("Choose a number "))
            break
        attempts+=1
        if guess==nrPC:
            print("Congrats u guessed the number in ", attempts, "/7 attempts")
            break
        else:
            if guess > nrPC:
                print("Too high ",attempts, "/7 attempts")
            elif guess < nrPC:
                print("Too low ",attempts, "/7 attempts")
    ans=input("Want to play again? Y/N")
    if ans in ["yes","Y","YES","Yes"]:
        pass
    elif ans in ["no","N","NO","No"]:
        exit()