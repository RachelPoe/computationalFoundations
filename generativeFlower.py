#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:18:16 2021

@author: rachelpoe
"""
# My generative art is 3 flowers with 5 petals each that are layered on top of each other
# My second turtle draws a circle near the origin
# The random library allows the petal colors to change at random each time I run my code

# import libraries
import turtle
import random

# create a window with green background color
panel = turtle.Screen()
turtle.colormode(255)
panel.bgcolor(60,179,113)

# define 2 turtles and define color list
flower = turtle.Turtle()
circle = turtle.Turtle()
flower.speed(0)
circle.speed(0)
colors = ["medium orchid","salmon","orange","hot pink"]


# make 3 flowers and determine the distance between each petal
# draw each petal using radians
# used random library to pick color of petals
for k in range (3):
    flower.right(72)
    flower.forward(50)
    for i in range(5):
        flower.ht()
        flower.color(random.choice(colors))
        flower.begin_fill()
        flower.circle(300,70)
        flower.left(110)
        flower.circle(300,70)
        flower.end_fill()
        
# make circle on origin
circle.up()
circle.ht()
circle.goto(0,0)
circle.color("gold")
circle.begin_fill()
circle.down()
circle.circle(50)
circle.end_fill()