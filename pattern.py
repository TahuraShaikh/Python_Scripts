#drawing random pattern:
import turtle
import random

cols=['blue','green','blue','red']

turtle.speed(3)

for c in range(20):
    x=random.randint(-100,100)
    y=random.randint(-100, 100)
    turtle.color(random.choice(cols))
    turtle.goto(x,y)