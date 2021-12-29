#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:41:09 2021

@author: Logan Turner, Rachel Poe, Campbell Mahan

Festive generative art that shows a series of light string and colored border.
Generative: light strand location, background color from list
Edge Interaction: border cycling through colors from list
How to Initialize Code: Press green play button at the top
"""

import turtle
import random

panel = turtle.Screen()
panel.clear()
w = 800 # width of panel
h = 800 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
turtle.tracer(0)
turtle.colormode(255)

running = True

#instantiate light strings
green = turtle.Turtle(shape='circle')#creates turtle
greenLights = 'lights1.gif' #assigns image to variable
panel.addshape(greenLights) #adds image to panel
green.shape(greenLights) #assigns image to turtle

red = turtle.Turtle(shape='circle')
redLights = 'lights4.gif'
panel.addshape(redLights)
red.shape(redLights)

yellow = turtle.Turtle(shape='circle')
yellowLights = 'lights2.gif'
panel.addshape(yellowLights)
yellow.shape(yellowLights)

blue = turtle.Turtle(shape='circle')
blueLights = 'lights3.gif'
panel.addshape(blueLights)
blue.shape(blueLights)

edgeColor = ['green','yellow','blue','red'] #list of edge colors

randomY = random.randint(-200,200) #randomly chooses number, which is later added to light string y value

bgColor = ['light green','light blue','pink'] #list of background colors
panel.bgcolor(random.choice(bgColor)) #randomly chooses color from list

#This class is used to draw the border around the window using a for loop.
class EDGE(turtle.Turtle):
    def __init__(self,x=0,y=0):
        super().__init__()
        self.ht()
        self.x = x
        self.y = y
        self.up()
        self.goto(-400,400)
        self.down()
        self.width(50)
        self.color(random.choice(edgeColor))
        for x in range(0,4):
            self.forward(800)
            self.right(90)
        
#This class is used to randomly stamp the light string images using the drawLights method.
class LIGHTS(turtle.Turtle):
    def __init__(self,x=0,y=0):
        super().__init__()
        self.ht()
        self.x=x
        self.y=y
        self.up()
        self.goto(0,0)
        self.drawLights()

#This method stamps each color's light string in a generative y location        
    def drawLights(self):
        #for i in range(0,4):
            green.ht()
            green.penup()
            green.goto(0,(150+randomY))
            green.stamp()
            
            red.ht()
            red.penup()
            red.goto(0,(-150+randomY))
            red.stamp()
            
            blue.ht()
            blue.penup()
            blue.goto(0,(-350+randomY))
            blue.stamp()
            
            yellow.ht()
            yellow.penup()
            yellow.goto(0,(350+randomY))
            yellow.stamp()

#this loop calls the EDGE and LIGHTS classes to actually enact the functions within them  
while running:
    EDGE()
    LIGHTS()
    panel.update()

turtle.done()