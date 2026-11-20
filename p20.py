# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:38:09 2026

@author: peterp
"""

from turtle import *

def main():
    setup(width=600,height=800) # sets the default width and height to 600x800
    bgcolor('gray')
    pensize(5)
    forward(100)
    penup()
    setposition(0,-150)
    fillcolor('white')
    begin_fill()
    pendown()
    circle(250) # size of the circle
    penup()
    
    setposition(-150,150)
    dot(100, 'white') # first eye ball
    
    setposition(150,150)
    dot(100, 'white') # second eye ball
    
    setposition(-150,150)
    dot(50, 'black') # first eye pupil
    
    setposition(150, 150)
    dot(50, 'black') #second eye pupil
    
    penup()
    setposition(0, 300)
    goto(-25, 100)
    pensize(5)
    pendown()
    forward(100) # nose
    pendown()
    setposition(0, 150)
    
    penup()
    goto(0, -150)
    pendown()           # neck
    goto(0, -500)
    penup()
main()
    
