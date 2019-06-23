from turtle import *
wn = Screen()
count = 10
angle = 180 + (count-2)*180/count
print(angle)

def shape(length):
	for i in range(count):
		forward(length)
		left(angle)

shape(100)
wn.exitonclick()
#This code is about shapes, just change the count value for your desired shape, 3 is triangle, 4 is square, 5 is pentagon etc

