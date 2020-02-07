import turtle as t
import time


window = t.Screen()
window.title("Happy Valentines Day")
window.bgcolor("black")
""""
# Sky : add a blue thing at the top
turtle.setpos(-400, 500)
turtle.color("blue")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

stamp_size = 20
square_size = 15
finish_line = 200
turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):  # creates a loop for ten squares and draws them 
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()
"""

x = 0
y = 0
start = 0,0
t.color('white')
t.down()
for j in range(5):
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    x += 50
    y += 50

# loop

t.setup(800,600,200,200)


def draw_shape(sides):
    t.pensize(3)
    t.pencolor("blue")
    for i in range(sides):
        t.right(360/sides)
        t.fd(200/sides)


x = -400
y = 200
for i in range(0,100):
    t.up()
    t.goto(x,y)
    t.down()
    draw_shape(i)
    x = x + 80
    print(x)
    if x > 400:
        x = x - 800
        y = y - 100
t.done()

