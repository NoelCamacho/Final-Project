# I used the tutorial from https://www.youtube.com/watch?v=miuHrP2O7Jw to guide me in this quest to make a final project 
import random
import time


# class Character():
#      def __init__(self):
#         self.dialogue1 = "Hello?"
#         self.dialogue2 = "Is anyone there?"
        # self.dialogue3 = 
        # self.dialogue4 =
        # self.dialogue5 =
        # self.dialogue =
        # self.dialogue7 =
        # self.dialogue8 =
        # self.dialogue9 =
# smith = Character()
# def say_dialogue1(self):
#     print(self.dialogue1)

def displayIntro():
    print("You awake in a cold, dark space ship to the sound of static")
    # time.sleep(2)
    print("The static seems to be coming from your walkie talkie")
    # time.sleep(2)
    print("You don't know who you are or how you got there")
    # time.sleep(2)
    print("Suddenly, you hear a voice on the walkie talkie asking for help")
    # time.sleep(2)
    print()


def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you answer the mysterious man or ignore him? (1 or 2): ")
#Prevents user from inputting anything other than 1 or 2. If anything else is inputted, the question will be asked again.

    return path  

def checkPath(chosenPath):
    print("After much hesitation you decide to...")
    # time.sleep(2)   

    
    correctPath =  (1)

    if chosenPath == str(correctPath) :
        print("Answer the man on the walkie talkie")
        # time.sleep(2)

    else:
        print("You ignore the man on the walkie talkie")
        # time.sleep(2)
        print("Never to hear from him again")
        # time.sleep(2)
        print("You dont find out who you are or how you got there, left to roam the galaxy lost and confused")
        # time.sleep(2)
        print()
#variable take so need new name, for simplicity Im just adding 2,3,etc at the end
def displayIntro2():
    print("Hello? Who's there?")
    # time.sleep(2)
    print("I'm hurt and I need some help")
    # time.sleep(2)
    print("Can you please help me?")

#choosePath already variable so need new name, for simplicity Im just adding 2,3,etc at the end
def choosePath2():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you ignore his plee for help or help him out? (1 or 2): ")
#Prevents user from inputting anything other than 1 or 2. If anything else is inputted, the question will be asked again.

    return path  
#checkPath already taken so new name has to be created
def checkPath2(chosenPath):
    print("")
    # time.sleep(2)   

    
    correctPath2 =  (2)

    if chosenPath == str(correctPath2) :
        print("You agree to help the man")
        # time.sleep(2)
        print("After some questions you figure out the man has a broken leg and a concussion")
        print()

    else:
        print("You refuse to help him")
        # time.sleep(2)
        print("One night you hear the man")
        # time.sleep(2)
        print("He seems to be saying his final words...")
        #time.sleep(2)
        print("A goodbye to his daughter and wife")
        print()































playAgain = "Yes"
while playAgain =="Yes" or playAgain == "Y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    #Choice is equal to "1" or "2"
    displayIntro2()
    choice = choosePath2()
    checkPath2(choice)
    playAgain = input("Do you want to play again?( Yes or Y to play again ) ")




