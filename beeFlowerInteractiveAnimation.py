#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/16/2021

@author: rachelpoe

Interactive animation where users can watch bee move across screen
and click to add a flower to the drawing.
"""

import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values

turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700 # set area of panel
h = 500
panel.setup(width=w, height=h)
panel.bgcolor(60,179,113) # make background green

# ================ VARIABLE DEFINITION & SETUP =========================
petals = turtle.Turtle() # name a turtle that draws petals
circle = turtle.Turtle() # name a turtle the draws the circle
petals.speed(0) # set turtle speeds
circle.speed(0)
colors = ["medium orchid","salmon","orange","hot pink"] # create list of colors for petals
running = True

bee = turtle.Turtle(shape="circle")
size = 4
running = True # while loop conditional
step = 1 # increment of ball movement (controls speed of bee)
count = 0 # edge crossingcounter, to determine when to stop animating
crosses = 10 # number of edge crosses to stop after

# import and set image as turtle shape
beeImg = "beegif.gif" # turtle library ONLY works with gifs!
panel.addshape(beeImg) # save the image to the panel so it knows what to draw
bee.shape(beeImg) # change the turtle shape to the saved image

bee.up()
# ================ FUNCTION DEFINITION =========================
def dot():
    '''draws circle over petals'''
    circle.up()
    circle.goto(0,0)
    circle.color("gold")
    circle.begin_fill()
    circle.down()
    circle.circle(50)
    circle.end_fill()
    
def flower(x,y):
    '''draws the flower petals
    Arguments: 
        x,y - to store location of click'''
    global petals # global variable
    for k in range (3):
        petals.right(72)
        petals.forward(50)
        for i in range(5):
            petals.color(random.choice(colors))
            petals.begin_fill()
            petals.circle(300,70)
            petals.left(110)
            petals.circle(300,70)
            petals.end_fill()
    circle()    
    bee.shape(beeImg)


# ================ ANIMATION LOOP =========================
panel.onclick(flower)
 
while running:
    bee.forward(step)
    xpos = bee.xcor() # get x position of bee

    if xpos >= w/2:
        # check if it crosses the RIGHT edge
        bee.goto(-w/2,0) # move it to the left edge
        count += 1 # keep track of the crossing
        
    if count > crosses:
        # check if we've made the intened number of crosses
        running= False
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



