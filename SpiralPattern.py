'''
My First Project using turtle Lib refered from insta -- python.hub page
Added to git

'''

import turtle

colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

t=turtle.Pen()

t.speed(100)


turtle.bgcolor("black")

for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.right(59)

turtle.done()
