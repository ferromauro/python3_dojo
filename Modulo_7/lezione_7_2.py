# Simple Pong Game Tutorial for Digital Dojo
# Check the course: 'Python 3 starter kit per sviluppatori' on wwww.digitaldojo.it

import turtle

wn = turtle.Screen()
wn.tracer(0)

wn.title("Dojo-Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)


t = turtle.Turtle()
t.pencolor('green')

for x in range(360):
    wn.update()
    t.width(x/100 + 1)
    t.forward(x)
    t.left(77)
        
