import turtle as t
import time as ti

a = ['cyan', 'blue', 'red', 'magenta', 'yellow', 'white']
t.bgcolor('black')
t.hideturtle()


while True:
    for i in a:
        t.color(i)
        t.dot(500)