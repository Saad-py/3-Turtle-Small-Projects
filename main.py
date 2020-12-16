# Imports
from turtle import *
import turtle as t
import time as ti




def illusion():
    t.speed(0)
    t.bgcolor('black')
    t.pensize(2)
    t.speed(0)

    for i in range(20):
        for colours in ['red', 'magenta', 'cyan', 'blue', 'green', 'yellow', 'white']:
            t.color(colours)
            t.circle(100)
            t.left(10)
            
    t.hideturtle()

    t.mainloop()

illusion()
