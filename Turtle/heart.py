from turtle import *

def curvemove(scale):
    size = scale
    scale = 1
    for x in range(200):
        right(1)
        forward(scale)

def heart(scale):
    seth(0)
    pendown()
    color('red','pink')
    begin_fill()
    left(140)
    forward(111.65*scale)
    curvemove(scale)
    left(120)
    curvemove(scale)
    forward(111.65*scale)
    end_fill()
    penup()


shapesize(0.01,0.01,0.01)

setpos(0,0)
heart(1)



ts = getscreen()
ts.getcanvas().postscript(file="heart.eps")
    
