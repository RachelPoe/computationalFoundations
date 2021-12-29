#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/8/2021

@author: Rachel Poe and Campbell Mahan

WHAT DOES YOUR GAME DO?
    OBJECTIVE - Click on the good guy and avoid the big bad turtle
    RULES - Do not click the bad turtle or you will lose the game
    CHALLENGE - The bad turtle blends with the background so the user cannot see it until after it is pressed
    INTERACTIONS - Click on the turtles, either win or lose depending on the turtle selected

"""
# To do: make enemies black and turn red, make screen black, create start screen, add run function
# Start screen says "How to Play: Click on a green turtle, avoid the black, hidden turtles

import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================


# ================ VARIABLE DEFINITION & SETUP =========================

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects.
# otherwise, try to include them in classes

# ================ CLASSES =========================

class Movers(turtle.Turtle):  # allows up to not have to name our turtle
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.shape('turtle')
        self.up()
        self.shapesize(3)
        self.color('forestgreen')
        self.goto(self.x, self.y)
        self.colorchange = "aliceblue"
        self.statement = "you got me!"
        global panel
        # onclick functions get called here!
        self.onclick(self.gotMe)

    # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!
    def walk(self):
        self.forward(random.randint(3, 20))
        self.seth(random.randint(0, 360))
        panel.update()

    def gotMe(self, x, y):
        global running
        self.color(self.colorchange)
        running = False
        print(self.statement)

# add new class here for enemies
# make enemies black so it's hard to see them and makes game harder, turn red if pressed


class Enemy(Movers, turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")  # change the turtle color to black
        self.shapesize(10)
        self.colorchange = "red"
        self.statement = "you lose!"


# ================ OBJECTS =========================
# instantiate objects here, object is an instance of a class
def setup():
    # all setup stuff after imports
    turtle.colormode(255)  # accept 0-255 RGB values
    turtle.tracer(0)  # turn off turtle's animation
    global panel
    panel = turtle.Screen()
    w = 800
    h = 800
    panel.setup(width=w, height=h)
    panel.bgcolor (0,0,0) # make background black

    word = turtle.Turtle()
    word.up()
    word.left(90)
    word.forward(250)
    word.left(90)
    word.forward(200)
    word.color("white")
    word.write("be careful, an evil turtle is on the loose!",
               font=("arial", 30, "normal"))
    run()


def run():
    global panel
    running = True
    instance = Movers(random.randint(-400, 400))
    enemy = Enemy()  # instantiate the enemies

    instanceList = []  # empty list
    for i in range(5):
        X = random.randint(-400, 400)  # each iteration. select random value
        instanceList.append(Movers(X))  # pass in to init method!


# ================ ANIMATION LOOP =========================
    while running:
        instance.walk()  # moving single instance
        enemy.walk()

        for inst in instanceList:
            inst.walk()

        panel.update()  # update the window with everything drawn in a single frame


# ================ CLEANUP =========================
setup()
turtle.mainloop()  # allows for user interactions; handles cleanup
