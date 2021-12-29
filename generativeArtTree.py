#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/8/2021

@author: Rachel Poe, Campbell Mahan, and Logan Turner

Festive generate art that features a christmas tree with flashing lights
Additionally, there are mini snowballs being throw around the screen randomly 
Generative: Screen background and lights on tree changes color
Edge Interaction: Snowballs bounce off edge of screen
How to Initialize Code: Press green play button at the top 

"""

import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================


# ================ VARIABLE DEFINITION & SETUP =========================\

w = 800
h = 800

randomColors = [(252,169,133), (255,250,129), (179,226,221), (11,183,214), (193,179,215), (251,182,209)] # generative
randomBackground = [(183,255,134), (162,255,134), (134,255,150), (144,238,144)]


# ================ FUNCTION DEFINITION =========================

# ================ CLASSES =========================

class Balls(turtle.Turtle): 
    """Snowballs class creates the snowballs on screen"""
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("circle") # sets turtle shape to circle
        self.up()
        self.shapesize(3)
        self.color('white') # sets color of balls to white
        self.goto(self.x, self.y)
        global panel, w, h # defines w & h as global variables to be accessed throughout code
        self.w = w
        self.h = h
        

    # ======== METHODS DEFINITIONS ==========
    
    def move(self): 
        """move method allows snowballs to be thrown around screen"""
        self.forward(100)
        self.seth(random.randint(0, 360)) # random location of throw
        panel.update()
        self.bounce()
        panel.update()
        
    def bounce(self): 
        """bounce method creates our edge interaction of bouncing back on screen"""
        x = self.xcor() # collect information on x cor of snowballs
        y = self.ycor() # collect information on y cor of snowballs
        heading = self.heading()
        
        if x < -self.w/2: #left side boundary 
            AOI = 0 - 2*heading # calcualates angle of incidence (AOI)
            self.seth(AOI)
            self.goto(-w/2+1,y) # snowballs bounce off edge
            return True 
        
        elif x > w/2: # right side boundary
            AOI = 180-2*heading 
            self.seth(AOI)
            self.goto(w/2-1, y)
            return True 
        
        elif y < -h/2: # top side boundary
            AOI = 270-2*heading
            self.goto(x,-h/2-1)
            self.seth(AOI)
            return True 
        
        elif y > h/2: # bottom side boundary
            AOI = 90-2*heading 
            self.goto(x, h/2-1)
            self.seth(AOI)
            return True 
        
        else: 
            return False # if the snowball is not hitting the edge it does not bounce
        
         
class Tree(turtle.Turtle): 
    """class to create tree in the middle of the screen"""
    def __init__(self, x=0, y=0): # parameters for location
        super().__init__()
        self.x = x
        self.y = y
        self.begin_fill()
        self.up()
        self.goto(-250,-200)
        self.ht()
        self.down()
        self.color("green")
        for x in range(0,3): # creates the triangle shape using a for loop 
            self.forward(500)
            self.left(120)
        self.end_fill()
        

class Trunk(turtle.Turtle): 
    """class to create trunk at the bottom of the tree shape"""
    def __init__(self, x=0, y=0): # parameters for location
        super().__init__()
        self.x = x
        self.y = y
        self.begin_fill() 
        self.up()
        self.goto(-50,-200) 
        self.ht()
        self.down()
        for x in range (0,4): # creates the square trunk shape using a for loop
            self.color("brown")
            self.forward(100)
            self.right(90)
        self.end_fill()
        

class Star(turtle.Turtle): 
    "class to create star at the top of the tree shape"""
    def __init__(self, x=0, y=0): # parameters for location
        super().__init__()
        self.x = x
        self.y = y
        self.up()
        self.goto(-75,220)
        self.ht()
        self.down()
        self.begin_fill()
        self.color("yellow")
        for x in range(0,5): # creates the star shape using a for loop
            self.forward(150)
            self.right(144)
        self.end_fill() # creates a shape that fills in the part of the star in the middle
        self.begin_fill()
        self.forward(150)
        self.right(144)
        self.forward(100)
        self.goto(-75,220)
        self.end_fill()


class Lights(turtle.Turtle): 
    """class to create circles that are flashing lights on the tree"""
    def __init__(self, x=0, y=0): # parameters for location
        super().__init__()
        self.x = x
        self.y = y
        self.up()
        self.goto(-280,-180)
        self.ht()
        self.down()
        self.color(random.choice(randomColors)) # uses a list to filter through creating the flashing pattern 
        for x in range(0,7): # creates the circle line using a for loop on the bottom of the tree
            self.up()
            self.forward(70)
            self.down()
            self.begin_fill()
            self.circle(15)
            self.end_fill()
        self.up()
        self.goto(-210,-90)
        self.down()
        for x in range(0,5): # creates the circle line using a for loop on the middle of the tree
            self.up()
            self.forward(70)
            self.down()
            self.begin_fill()
            self.circle(15)
            self.end_fill()
        self.up()
        self.goto(-170,0)
        self.down()
        for x in range(0,4): # creates the circle line using a for loop on the middle of the tree
            self.up()
            self.forward(70)
            self.down()
            self.begin_fill()
            self.circle(15)
            self.end_fill()
        self.up()
        self.goto(-140,80)
        self.down()
        for x in range(0,3): # creates the circle line using a for loop on the top of the tree
            self.up()
            self.forward(70)
            self.down()
            self.begin_fill()
            self.circle(15)
            self.end_fill()
    
 

# ================ OBJECTS =========================
def setup(): 
    """manager"""
    turtle.colormode(255)  # accept 0-255 RGB values
    turtle.tracer(0)  # turn off turtle's animation
    global panel
    panel = turtle.Screen()
    w = 800
    h = 800
    panel.setup(width=w, height=h)
    panel.bgcolor(random.choice(randomBackground)) # make background color random based on the list of greens

    run()


def run(): 
    """manager"""
    global panel
    running = True
    instance = Balls(random.randint(-400, 400)) # random throw of snowballs

    instanceList = []  # empty list
    for i in range(5):
        X = random.randint(-400, 400)  # each iteration. select random value
        instanceList.append(Balls(X))  # pass in to init method!

    while running:
        instance.move()
        Tree() # create object of Tree, instantiating the class
        Trunk() # create object of Trunk, instantiating the class
        Lights() # create object of Lights, instantiating the class
        Star() # create object of Star, instantiating the class
        
    
        for inst in instanceList:
            inst.move() # instantiating the Balls class
    
        panel.update()
        
# ================ ANIMATION LOOP =========================
setup()

# ================ CLEANUP =========================

turtle.mainloop()  # allows for user interactions; handles cleanup
