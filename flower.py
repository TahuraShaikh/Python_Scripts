import turtle
ts = turtle.Turtle()
ts.color("red","blue")
ts.speed(10)
ts.begin_fill()
for i in range(25):
    ts.forward(300)
    ts.left(165)
ts.end_fill()
turtle.done()