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

# House
t.setheading(0)
t.penup()
t.goto(-100, -200)
t.pendown()
t.color("saddlebrown")
t.begin_fill()
for i in range(2):
    t.fd(200)
    t.left(90)
    t.fd(250)
    t.left(90)
t.end_fill()

# Σκεπή
t.penup()
t.goto(-100, 50)
t.pendown()
t.setheading(0)
t.color("red")
t.begin_fill()
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
t.fd(200)
t.end_fill()

t.hideturtle()
turtle.done()