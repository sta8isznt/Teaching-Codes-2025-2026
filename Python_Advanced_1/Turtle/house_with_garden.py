import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Grass
t.penup()
t.goto(-400, -200)

t.color("green")
t.begin_fill()
t.right(90)
t.fd(200)
t.left(90)
t.fd(800)
t.left(90)
t.fd(200)
t.left(90)
t.fd(800)
t.end_fill()

t.hideturtle()
turtle.done()