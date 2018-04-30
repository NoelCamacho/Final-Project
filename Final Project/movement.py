# import turtle
# from time import sleep
# import threading
# import time

# # #Setting up the screen  
# wn = turtle.Screen()
# wn.bgcolor("white")
# wn.title("Battle Grounds")

# # #Creating our player
# player = turtle.Turtle()
# player.color("indigo")
# player.shape("triangle")
# # player.image("man.jpeg")
# # class Man():
# #     def __init__(self, name, tool, speed, heading, up, left, down, right, turtleClass):
# #         self.name = name
# #         self.tool = tool
# #         self.speed = speed
# #         self.heading = heading
# #         self.turtleClass = Turtle()
# #         self.up = up
# #         self.left = left
# #         self.down = down
# #         self.right = right
# #         self.screen = self.turtleClass.getscreen()
# #     def printName(self):
# #         print(self.name)
# #     def playerSetup(self):
# #         # #leoscreen.addshape(leo['image'])
# #         # #leo['turtle'].shape(leo['image'])
# #         # leo['turtle'].penup()
# #         # leo['turtle'].shape('turtle')
# #         # leo['turtle'].color(leo['color'])
# #         def attack(self):
# #             print(self.name + " just used his " + self.weapon + ".")
# #         self.turtleClass.setheading(self.heading)
# #         self.turtleClass.color(self.color)
# #         self.turtleClass.forward(300)
# #     def check(self):
# #             if self.turtleClass.xcor() > 300 or self.turtleClass.xcor() < -300 or self.turtleClass.ycor() < -300 or self.turtleClass.ycor() > 300:
# #                 #to allow us to use the global version of hitpoints, we use 'global'
# #                 #we need to have this or the variable is considered to be of local scope
# #                 global hitpoints
# #                 print("Out of x or bounds!!!")
# #                 # longhand hitpoints = hitpoints - 10
# #                 self.hp-=10
# #                 print(self.hp)
# #                 if self.hp <= 0:
# #                     print("he's dead jim")
# #                     sleep(3)
# #                     self.screen.bye()

# def movement(self):
#                 def w():
#                     self.turtleClass.setheading(90)
#                     self.turtleClass.forward(self.speed)
#                     self.check()
# def a():
#             self.turtleClass.setheading(180)
#             self.turtleClass.forward(self.speed)
#             self.check()
# def s():
#             self.turtleClass.setheading(270)
#             self.turtleClass.forward(self.speed)
#             self.check()
# def d():
#             self.turtleClass.setheading(0)
#             self.turtleClass.forward(self.speed)
#             self.check()
# self.screen.onkeypress(w, self.up)
# self.screen.onkeypress(a, self.left)
# self.screen.onkeypress(s, self.down)
# self.screen.onkeypress(d, self.right)
# self.screen.listen()








# sleep(5)













# # class Archer():
# #     def __init__(self, name, color, weapon, hp, speed, heading, image, up, left, down, right):
# #         self.name = name
# #         self.color = color
# #         self.weapon = weapon
# #         self.hp = hp
# #         self.speed = speed
# #         self.heading = heading
# #         self.image = image
# #         self.turtleClass = Turtle()
# #         self.up = up
# #         self.left = left
# #         self.down = down
# #         self.right = right
# #         self.screen = self.turtleClass.getscreen()


# # class Farmer(turtle.Turtle):



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