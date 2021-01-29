#using recursion
import turtle
ts=turtle.Turtle()
ts.getscreen().bgcolor("#9FE2BF")          #background color
ts.speed(10)
ts.penup()
ts.goto((-200,100))            # for giving location
ts.pendown()
def star (turtle,size):
    if size <=10:               # star will be very small
        return
    else :
        turtle.begin_fill()
        for i in range(5):                # for star
            turtle.forward(size)
            star(turtle,size/3) #calls star of smaller size
            turtle.left(216)
        turtle.end_fill()

star(ts,360)
turtle.done()