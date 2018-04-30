from turtle import *
from time import sleep
import threading
import time


userInput= input("Welcome, what is your name? ")
print("Welcome" + "," + " " + (userInput) + "," + " " + "to the Battle of Gods ")
# input("Choose a Class ")
t = ["Rock", "Paper", "Scissors"]
class Archer():
    def __init__(self, name, color, weapon, hp, speed, heading, image, up, left, down, right):
        self.name = name
        self.color = color
        self.weapon = weapon
        self.hp = hp
        self.speed = speed
        self.heading = heading
        self.image = image
        self.turtleClass = Turtle()
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.screen = self.turtleClass.getscreen()

        