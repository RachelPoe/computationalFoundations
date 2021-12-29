#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/8/2021

@author: Rachel Poe, Campbell Mahan, and Logan Turner

Festive generate art that shows a spiral snowflake in the center of the panel
Additionally, there are mini snowballs being throw around the screen randomly 
Generative: Screen changes color each time code is ran
Edge Interaction: Snowballs bounce off the edge of the screen
How to Initialize Code: Press the green play button at the top

"""

import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================


# ================ VARIABLE DEFINITION & SETUP =========================\

w = 800
h = 800

randomColors = [(164,179,232), (153,204,255), (204,229,255), (171,208,245)]
randomBackground = [(48,57,188), (21,80,240), (42,15,179), (30,6,152), (49,10,247)] # generative

# ================ FUNCTION DEFINITION =========================

# ================ CLASSES =========================

class Balls(turtle.Turtle): 
    """Snowballs class creates the snowballs on the screen""" 
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
        
        
        
class Snowflake(turtle.Turtle): 
    """class to create snowflake in the middle of the screen"""
    def __init__(self, x=0, y=0): # parameters for location
        super().__init__()
        self.x = x
        self.y = y
        for x in range(0,12): # for loop the iterates to create snowflake
            self.color(random.choice(randomColors)) # uses a list to filter through creating the flashing pattern 
            self.width(10)
            self.circle(125)
            self.left(30)
        

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
    panel.bgcolor(random.choice(randomBackground)) # make background color random based on the list of blues

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
        Snowflake() # create object of Snowflake, instantiating the class
        
    
        for inst in instanceList:
            inst.move() # instantiating the Balls class
    
        panel.update()
        
# ================ ANIMATION LOOP =========================
setup()

# ================ CLEANUP =========================

turtle.mainloop()  # allows for user interactions; handles cleanup
