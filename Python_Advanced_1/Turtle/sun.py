import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("blue")
t.speed(0)

t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0, 100)
for i in range(36):
    t.forward(100)
    t.pendown()
    t.forward(80)
    t.penup()
    t.goto(0,100)
    t.right(10)


turtle.done()