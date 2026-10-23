import turtle

t = turtle
t.speed(15)
t.pensize(2)

screen = turtle.Screen()
screen.bgcolor('black')

t.begin_fill()
t.color('orange')
t.circle(75,360)
t.end_fill()

t.color('brown')
t.penup()
t.goto(-35,8)
t.left(90)
t.pendown()
t.forward(137)
t.penup()
t.right(90)
t.forward(69)
t.right(90)
t.pendown()
t.forward(137)
t.penup()
t.color('black')
t.goto(-13,59)
t.left(90)
t.pendown()
t.begin_fill()

for x in range(3):
    t.forward(25)
    t.left(120)

t.end_fill()
t.penup()
t.goto(-45,90)
t.pendown()
t.begin_fill()

for x in range(3):
    t.forward(30)
    t.left(120)

t.end_fill()
t.penup()
t.forward(58)
t.pendown()
t.begin_fill()

for x in range(3):
    t.forward(30)
    t.left(120)

t.end_fill()
t.penup()
t.goto(-50,27)
t.right(17)
t.pendown()
t.begin_fill()

for x in range(3):
    t.forward(25)
    t.left(120)

t.end_fill()
t.penup()
t.left(17)
t.goto(-33,20)
t.pendown()
t.begin_fill()

for x in range(3):
    for x in range(3):
        t.forward(23)
        t.left(120)
    t.forward(20)
    
t.end_fill()
t.penup()
t.left(17)
t.forward(-3)
t.pendown()
t.begin_fill()

for x in range(3):
    t.forward(25)
    t.left(120)

t.end_fill()
t.penup()
t.color('green')
t.goto(-5,150)
t.left(73)
t.begin_fill()
t.pendown()
t.forward(40)
t.right(90)
t.forward(10)
t.right(90)
t.forward(40)
t.right(90)
t.forward(10)
t.end_fill()
t.color('orange')
t.penup()
t.goto(0,-20)
t.write(
    "happy halloween",
    align="center",
    font=("arial",15, "bold")
)    
t.goto(0,-45)
t.write(
    "tonmai",
    align="center",
    font=("arial",15, "bold")
)    
t.hideturtle()
turtle.done()
