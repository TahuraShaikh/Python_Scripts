import turtle   # libraries imported
import time
turtle.mode('logo')        # clock moves in clockwise direction
'''Hour hand'''
h=turtle.Turtle()   # creates hour hand
h.color('red')            # hand will be in red color
h.shape('arrow')        # hour hand will be arrow shaped
h.shapesize(1,8)      # hand will be 8 times longer than normal
'''Minute hand'''
m=turtle.Turtle()   # creates minute hand
m.color('blue')            # hand will be in blue color
m.shape('arrow')        # minute hand will be arrow shaped
m.shapesize(1,12)        # hand will be 12 times longer than normal
'''Second hand'''
s=turtle.Turtle()   # creates second hand
s.color('green')            # hand will be in green color
s.shape('arrow')        # second hand will be arrow shaped
s.shapesize(1,13)        # hand will be 13 times longer than normal

def hands():             #function which draws hands
    t=time.localtime()    # local time stored in variable t
    s.seth(t.tm_sec*6)       # angle of seconds hand set
    m.seth(t.tm_min * 6)    # angle of minute hand set
    h.seth(t.tm_hour*30 + t.tm_min*0.5)     # angle of hour hand set
    turtle.ontimer(hands,1000)          # function repeats after 1000 milliseconds(1 second later)

hands()           # hands function will be run
