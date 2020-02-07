""""# Python Turtle - WordArt Challenge - www.101computing.net/python-turtle-wordart-challenge/
import turtle
import random
from alphabet import alphabet

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
#window.bgcolor("#000000")
myPen.pensize(2)


def displayMessage(message, fontSize, color, x, y):
    myPen.color(color)
    message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            myPen.penup()
            for dot in letter:
                myPen.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
                myPen.pendown()

            x += fontSize

        if character == " ":
            x += fontSize
        x += characterSpacing

    # Main Program Starts Here


fontSize = 10
characterSpacing = 5
fontColor = "#FF00FF"

#message = "Hello world!"
message = ""
displayMessage(message, fontSize, fontColor, -190, 0)
turtle.done()

"""
# Python Turtle - WordArt Challenge - www.101computing.net/python-turtle-wordart-challenge/
import turtle  # import the turtle module
import random  # a function to create random instances
from alphabet import alphabet  # the other module which has the coordinates.

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)  # penspeed, doesnt have an animation.
# window = turtle.Screen()  # do not need a screen, opening our own module.
#window.bgcolor("#000000")
myPen.pensize(2)  # size of the pen


def displayMessage(message, fontSize, color, x, y):  # creating a module that displays the message using font size, colour and the message that is input.
    myPen.color(color)  # choose the colour
    #message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            myPen.penup()
            for dot in letter:
                myPen.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
                myPen.pendown()

            x += fontSize

        if character == " ":
            x += fontSize
        x += characterSpacing

    # Main Program Starts Here


fontSize = 10
characterSpacing = 5
fontColor = "black"
