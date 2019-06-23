from turtle import *
import random

speed(0)
bgcolor("Black")
color('blue')

colorlist = ['white', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

def shape(length,side):
    angle= 180-(((side-2)*180)/side)
    for count in range(side):
        forward(length)
        left(angle)

def rotation():
    n = 0
    for count in range(3600):
    	color(colorlist[random.randint(0,6)])
    	shape(n,6)
    	n += 1
    	left(3)


penup()
goto(0,0)
pendown()

rotation()

hideturtle()
done()
