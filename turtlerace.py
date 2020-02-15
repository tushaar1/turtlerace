import time
import turtle
from turtle import *
import letters
import turtleracestart
from random import randint, choice


# Turtle Race Window and initial start.
def start():
    window = turtle.Screen()
    window.title("Turtle Race")
    turtle.bgcolor("forestgreen")
    turtle.hideturtle()
    turtle.speed(0)
    letters.displayMessage("WELCOME TO TURTLE RACE", 10, "black", -140, 200)
    turtleracestart.startseq()
    time.sleep(2)
    turtle.clearscreen()


def therace():
    turtle.bgcolor("forestgreen")
    turtle.penup()

    # Dirt
    turtle.setpos(-400, -180)
    turtle.color("brown")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.penup()
    turtle.end_fill()

    # Sky : add a blue thing at the top
    turtle.setpos(-400, 450)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(250)
    turtle.end_fill()

    # Finish Line
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

    for j in range(10):
        turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
        turtle.stamp()
    turtle.hideturtle()

    # Header
    turtle.color("white")  # text colour
    turtle.speed(0)  # speed of the animation
    turtle.penup()  # moving the position that we have.
    turtle.setpos(-130, 200)  # setpos sets the postion of the turtle
    turtle.write("Turtle Race", font=("Arial", 30, "bold"))


def race():
    # Turtle 1
    turtle1 = Turtle()
    turtle1.speed(0)
    turtle1.color("red")
    turtle1.shape("turtle")
    turtle1.penup()
    turtle1.goto(-250, 100)
    turtle1.pendown()

    # Turtle 2
    turtle2 = Turtle()
    turtle2.speed(0)
    turtle2.color("cyan")
    turtle2.shape("turtle")
    turtle2.penup()
    turtle2.goto(-250, 50)
    turtle2.pendown()

    # Turtle 3
    turtle3 = Turtle()
    turtle3.speed(0)
    turtle3.color("magenta")
    turtle3.shape("turtle")
    turtle3.penup()
    turtle3.goto(-250, 0)
    turtle3.pendown()

    # Turtle 4
    turtle4 = Turtle()
    turtle4.speed(0)
    turtle4.color("brown")
    turtle4.shape("turtle")
    turtle4.penup()
    turtle4.goto(-250, -50)
    turtle4.pendown()

    # Turtle 5
    turtle5 = Turtle()
    turtle5.speed(0)
    turtle5.color("yellow")
    turtle5.shape("turtle")
    turtle5.penup()
    turtle5.goto(-250, -100)
    turtle5.pendown()

    time.sleep(1)  # pause the game for a sec before starting it

    # Race time
    for i in range(80):
        turtle1.forward(randint(1, 10))
        turtle2.forward(randint(1, 10))
        turtle3.forward(randint(1, 10))
        turtle4.forward(randint(1, 10))
        turtle5.forward(randint(1, 10))




start()
therace()
race()
turtle.done()

