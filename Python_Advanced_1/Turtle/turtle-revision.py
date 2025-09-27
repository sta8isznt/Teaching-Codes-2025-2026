import turtle

screen = turtle.Screen()
nikos  = turtle.Turtle()

nikos.forward(100)
nikos.backward()
nikos.right(90)
nikos.left()

nikos.fd()

# Χρώμα γραμμής
nikos.pencolor("red")

# Χρώμα γεμίσματος
nikos.fillcolor("yellow")

nikos.penup()
nikos.goto(100, 200)
nikos.pendown()

# Ταχύτητα
nikos.speed(0)

# Γέμισμα με χρώμα
nikos.begin_fill()
# σχέδιο
nikos.end_fill()

nikos.circle(10)

# Κρύψημο χελώνας
nikos.hideturtle()