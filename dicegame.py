import random as rnd
print("Welcome to the dice game")
playAgain = True;
while(playAgain):
    lowRange = input("Enter the lower range of the dice: ")
    highRange = input("Enter the higher range of the dice: ")
    if(highRange <= lowRange):
        print("High range must be higher than the low range by at least one!")
        continue
    print(lowRange)
    print(highRange)
    randVal = rnd.randint(int(lowRange), int(highRange))
    print("The dice rolled: " + str(randVal))
    response = input("Do you want to play again (enter y for yes, or n for no): ")
    if (response == "n"):
        playAgain =False
