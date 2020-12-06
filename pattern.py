#drawing random pattern:
import turtle     # turtle library
import random     #random library

cols=['blue','green','blue','red']             # list of colours to use

turtle.speed(3)            # speed of turtle

for c in range(50):          # loop can be changed
    x=random.randint(-100,100)      # variables x & y with random values from -100 to 100
    y=random.randint(-100, 100)
    turtle.color(random.choice(cols))        # turtle is set to random color
    turtle.goto(x,y)     # turtle will goto random x & y values