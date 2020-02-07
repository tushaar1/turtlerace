import turtle
from turtle import Turtle
import time


def startseq():
    sTurtle1 = Turtle()
    sTurtle1.color("red")
    sTurtle1.shape("turtle")
    sTurtle1.penup()
    sTurtle1.goto(-50, 100)
    sTurtle1.pendown()

    sTurtle2 = Turtle()
    sTurtle2.color("cyan")
    sTurtle2.shape("turtle")
    sTurtle2.penup()
    sTurtle2.goto(-0, 100)
    sTurtle2.pendown()

    sTurtle3 = Turtle()
    sTurtle3.color("magenta")
    sTurtle3.shape("turtle")
    sTurtle3.penup()
    sTurtle3.goto(50, 100)
    sTurtle3.pendown()

    time.sleep(1)

    for i in range(7):
        sTurtle1.right(180)
        sTurtle2.right(90)
        sTurtle3.right(360)
    for i in range(20):
        sTurtle1.forward(10)
        sTurtle2.forward(10)
        sTurtle3.forward(10)