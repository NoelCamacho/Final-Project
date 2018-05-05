# I used the tutorial from https://www.youtube.com/watch?v=miuHrP2O7Jw to guide me in this quest to make a final project 
import random
import time

def displayIntro():
    #print("You awake in a dark, mysterious room lit with nothing but a candle in a corner of the room.")
    #print("Armed with nothing but your wits and ")
    print("It is the end of a long year of fighting space criminals")
    print("You come to crossroads on your trip home, one path leads home")
    print("where you will be handsomely rewarded for a job well done")
    print("and the other leads through a gamma ray burst that will disentigrate you")
    print()


def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path with you choose? (1 or 2): ")
#Prevents user from inputting anything other than 1 or 2. If anything else is inputted, the question will be asked again.

    return path  

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("There is an asteriod nearby that looks familiar that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep()
    
    correctPath = random.randint (1,2)

    if chosenPath == correctPath:
        print("That tingling was just the feeling of admiration from the citizens of the galaxy")
        print("Welcome home")
    else:
        print("At extremely energetic burst of gamma rays blast threw you")
        print("Causing all of the atoms in your body to dissociate")
        print("There is no record left of your existence")


    displayIntro()
choosePath()