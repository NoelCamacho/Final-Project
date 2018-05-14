# I used the tutorial from https://www.youtube.com/watch?v=miuHrP2O7Jw to guide me in this quest to make a final project 
import random
import time
import sys


def displayIntro():
    print("You awake in a cold, dark spaceship escape pod to the sound of static")
    time.sleep(2)
    print("The static seems to be coming from your radio")
    time.sleep(2)
    print("You don't know who you are or how you got there")
    time.sleep(2)
    print("Suddenly, you hear a voice on the radio asking for help")
    time.sleep(2)
    print()
def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you answer the mysterious man or ignore him? (1 or 2): ")
#Prevents user from inputting anything other than 1 or 2. If anything else is inputted, the question will be asked again.
    return path  
def checkPath(chosenPath):
    print("After much hesitation you decide to...")
    time.sleep(2)   
    correctPath =  (1)
    if chosenPath == str(correctPath) :
        print("Answer the man on the radio")
        time.sleep(2)
    else:
        print("You ignore the man on the radio")
        time.sleep(2)
        print("Never to hear from him again")
        time.sleep(2)
        print("You dont find out who you are or how you got there, left to roam the galaxy lost and confused")
        time.sleep(2)
        sys.exit()
        #sys.exit() is used to end the program if the 'wrong' option is chosen instead of the code continuing
#variable take so need new name, for simplicity Im just adding 2,3,etc at the end
def displayIntro2():
    print("He is asking for help")
    time.sleep(2)
    print("He introduces himself as Smith, a mechanic hired to overlook all of the ships problems")
    print()
#choosePath already variable so need new name, for simplicity Im just adding 2,3,etc at the end
def choosePath2():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you ignore his plee for help or help him out? (1 or 2): ")
#Prevents user from inputting anything other than 1 or 2. If anything else is inputted, the question will be asked again.
    return path  
#checkPath already taken so new name has to be created
def checkPath2(chosenPath):
    # print("")
    time.sleep(2)    
    correctPath2 =  (2)
    if chosenPath == str(correctPath2) :
        print("You agree to help the man")
        time.sleep(2)
        print("He tells you he has a broken leg and a concussion")
        time.sleep(2)
    else:
        print("You refuse to help him")
        time.sleep(2)
        print("One night you hear the man")
        time.sleep(2)
        print("He seems to be saying his final words...")
        time.sleep(2)
        print("A goodbye to his daughter and wife")
        sys.exit()
def displayIntro3():
    print("Before you embark on your journey to help him, you ask him some more questions.")
    time.sleep(2)
    print("You learn you were part of a space mission called Operation Cerberus to colonize the planets known as Cerberus I, Cerberus II and Cerberus III")
    time.sleep(2)
    print("These names were given to the planets because the 3 planets orbit themselves, making it seem as if they are attached")
    time.sleep(2)
    print("There were originally 100 people on your voyage")
    time.sleep(2)
    print("There was an explosion that killed almost everyone, except a lucky few that managed to escape.")
    time.sleep(2)
def displayIntro4():
    print("You are thought to be on Cerberus II")
    time.sleep(2)
    print("You check the fuel, and only have enough fuel to travel to Cerberus I or Cerberus III")
    time.sleep(2)
    print()
def choosePath4():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you travel to Cerberus I or Cerberus III? (1 or 2): ")
    return path  
def checkPath4(chosenPath):
    print("You land on the planet")
    time.sleep(2)
    correctPath = random.randint (1,2)
    #Makes 1 or 2 the correct path, for variety everytime the game is played
    if chosenPath == str(correctPath) :
        print("As you start landing, you see an escape pod")
        time.sleep(2)
        print("You head towards the escape pod hoping to find Smith")
        ###time.sleep
        print("You find Smith")
        time.sleep(2)
        
    else:
        print("You search the planet")
        time.sleep(2)
        print("You only find remnants of the ship you were on")
        time.sleep(2)
        print("There is not enough fuel to travel again")
        time.sleep(2)
        print("You are stuck there until the end of time")
        sys.exit()
def displayIntro5():
    print("Smith's leg is snapped in two")
    time.sleep(2)
    print("He appears to be losing a lot of blood")
    time.sleep(2)
    print("You must take him to your pod for him to survive")
    time.sleep(2)
def choosePath5():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you carry or drag him to your pod? (1 or 2): ")
    return path  
def checkPath5(chosenPath):
    print("")
    time.sleep(2)
    correctPath = random.randint (1,2)
    #Makes 1 or 2 the correct path, so there is no set path
    if chosenPath == str(correctPath) :
        print("You successfully make it to your pod where you tend to his wounds")
        time.sleep(2)
        print("You stop his bleeding")
        time.sleep(2)
    else:
        print("While making your way to your pod you stumble and fall")
        time.sleep(2)
        print("While falling, you crack your head open on rock")
        time.sleep(2)
        print("Smith is flabbergasted, not knowing what just happened.")
        time.sleep(2)
        print("Smith dies later that day from blood loss")
        time.sleep(2)
        sys.exit()
def displayIntro6():
    print("After a few days of being on this miserable planet")
    time.sleep(2)
    print("You hear a voice through your radio")
    time.sleep(2)
    print("A rescue ship has come to search for survivors")
    time.sleep(2)
    print("You only have a few hours before it leaves")
    time.sleep(2)
    print("You use two flares to try getting the ships attention with no avail")
def choosePath6():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you light a fire or use your 1 remaining flare? (1 or 2): ")
    return path  
def checkPath6(chosenPath):
    print("")
    time.sleep(2)
    correctPath = random.randint (1,2)
    #Makes 1 or 2 the correct path, so there is no set path
    if chosenPath == str(correctPath) :
        print("You get the ships attention")
        time.sleep(2)
        print("Over the radio you are informed that the ship cannot come to you due to a storm that is headed your way")
        time.sleep(2)
        print("You must make it to the ship yourself")
        time.sleep(2)
    else:
        print("That does not seem to get the ships attention")
        time.sleep(2)
        print("You two quickly try the other option")
        time.sleep(2)
        print("You see the ships turning the other way")
        time.sleep(2)
        print("It is too late. Your only chance to leave this planet has left")
        time.sleep(2)
        sys.exit()
def displayIntro7():
    print("Wth limited time, you must find a way to make it to the ship")
    time.sleep(2)
    print("With the remaining fuel on your pod and the fuel in Smith's pod, there is almost enough to make it")
    time.sleep(2)
    print("You must get rid of some weight")
    time.sleep(2)

def choosePath7():
    path = ""
    while path != "1" and path != "2":
        path = input("Do you remove the autopilot command console box or the captains seat/controls(1 or 2): ")
    return path  
def checkPath7(chosenPath):
    print("")
    time.sleep(2)
    correctPath = random.randint (1,2)
    if chosenPath == str(correctPath) :
        print("With the help of what could only be described as a divine power, you make it to the ship")
        time.sleep(2)
        print("As you're boarding the ship, you see no other survivors")
        time.sleep(2)
        print("Smith lets out a sigh of relieve")
        time.sleep(2)
        print("You two were the only lucky ones")
        time.sleep(2)
    else:
        print("As you are making your way to the ship")
        time.sleep(2)
        print("Your ship starts to buckle under the immense pressure")
        time.sleep(2)
        print("With no way to control it, your ship goes off course")
        time.sleep(2)
        print("The ship goes back into orbit and starts plummeting back onto the planet")
        time.sleep(2)
        print("You say your goodbye's until the second you crash")
        time.sleep(2)
        print("Neither of you make it...")
        sys.exit()
def displayIntro8():
    print()
    print("With your adventure coming to an end, you let out a deep sigh and rest your eyes")
    time.sleep(3)
    print("The End")
playAgain = "Yes"
while playAgain =="Yes" or playAgain == "Y":
    displayIntro()
    #displays the texy
    choice = choosePath()
    #Telling us the 
    checkPath(choice)
    #Choice is equal to "1" or "2"
    displayIntro2()
    choice = choosePath2()
    checkPath2(choice)
    displayIntro3()
    displayIntro4()
    choice = choosePath4()
    checkPath4(choice)
    displayIntro5()
    choice = choosePath5()
    checkPath5(choice)
    displayIntro6()
    choice = choosePath6()
    checkPath6(choice)
    displayIntro7()
    choice = choosePath7()
    checkPath7(choice)
    displayIntro8()
    playAgain = input("Do you want to play again?( Yes or Y to play again ) ")