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

t.penup()
t.goto(50, 120)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-50, 120)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Smile
t.penup()
t.goto(-50, 70)
t.setheading(-60) # new
t.pendown()
t.width(4)
t.circle(60, 120)

t.hideturtle()
turtle.done()