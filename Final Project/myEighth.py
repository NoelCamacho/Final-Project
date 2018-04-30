# #this file was created by Noel Camacho

# Noel = {
#     'name': 'Noel'
#     'age': '16'
#     'eyeColor': 'brown'
# }


# #classes
# class Dog()
#     def__init__(self, name, age):
#     self.name = name
#     self.age  = age
#     def sit(self):
#         print(self.name.title() + " is now sitting."
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")

# scooby = ("scooby", 3)

# # classes
# class Dog():
#     def __init__(self, age, breed):
#         self.age = age
#         self.breed = breed
#     def sit(self):
#         print(self.name.title() + " is now sitting. He is a " + self.breed)
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")
# # class lizard():
# #     def __init__(self, name, )

# scooby = Dog(3, "lab")
# scooby.age = 4
# scrappy = Dog(1, "pug")
# print(scooby.name)






















from turtle import *
from time import sleep
import threading
import time

class ninjaTurtle():
    def __init__(self, name, color, weapon, hp, speed, heading, up, left, down, right, turtleClass):
        self.name = name
        self.color = color
        self.weapon = weapon
        self.hp = hp
        self.speed = speed
        self.heading = heading
        self.turtleClass = Turtle()
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.screen = self.turtleClass.getscreen()
    def printName(self):
        print(self.name)
    def playerSetup(self):
        # #leoscreen.addshape(leo['image'])
        # #leo['turtle'].shape(leo['image'])
        # leo['turtle'].penup()
        # leo['turtle'].shape('turtle')
        # leo['turtle'].color(leo['color'])
    def attack(self):
        print(self.name + " just used his " + self.weapon + ".")
        self.turtleClass.setheading(self.heading)
        self.turtleClass.color(self.color)
        self.turtleClass.forward(300)
    def check(self):
            if self.turtleClass.xcor() > 300 or self.turtleClass.xcor() < -300 or self.turtleClass.ycor() < -300 or self.turtleClass.ycor() > 300:
                #to allow us to use the global version of hitpoints, we use 'global'
                #we need to have this or the variable is considered to be of local scope
                global hitpoints
                print("Out of x or bounds!!!")
                # longhand hitpoints = hitpoints - 10
                self.hp-=10
                print(self.hp)
                if self.hp <= 0:
                    print("he's dead jim")
                    sleep(3)
                    self.screen.bye()
    def movement(self):
        def w():
            self.turtleClass.setheading(90)
            self.turtleClass.forward(self.speed)
            self.check()
        def a():
            self.turtleClass.setheading(180)
            self.turtleClass.forward(self.speed)
            self.check()
        def s():
            self.turtleClass.setheading(270)
            self.turtleClass.forward(self.speed)
            self.check()
        def d():
            self.turtleClass.setheading(0)
            self.turtleClass.forward(self.speed)
            self.check()
        self.screen.onkeypress(w, self.up)
        self.screen.onkeypress(a, self.left)
        self.screen.onkeypress(s, self.down)
        self.screen.onkeypress(d, self.right)
        self.screen.listen()
        
    
leo = ninjaTurtle("leo", "blue", "katana", 100, 6, 90, "w","a","s","d","")
don = ninjaTurtle("don", "purple", "bo", 100, 8, 90, "Up", "Left", "Down", "Right", "" )
leo.playerSetup()
leo.movement()
don.playerSetup()
don.movement()
done()





from turtle import *
from time import sleep
import threading
import time

class superHero():
    def __init__(self, name, color, weapon, hp, speed, heading, image, up, left, down, right, superHeor):
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
        self.screen = self.superHero.getscreen()
    def printName(self):
        print(self.name)
    def playerSetup(self):
        self.screen.addshape(self.image)
        self.turtleClass.shape(self.image)

batman = superHero(batman, black, money, 70, 100, 70, image, "w", "a", "s", "d", "")