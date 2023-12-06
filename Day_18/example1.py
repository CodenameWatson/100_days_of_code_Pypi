import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tur = Turtle()
tur.shape("turtle")
tur.color("purple")

#Draw Square
# for _ in range(4):
#     tur.fd(100)
#     tur.rt(90)



#Draw Dashed line
# for _ in range(50):
#     tur.pendown()
#     tur.fd(10)
#     tur.penup()
#     tur.fd(10)
def get_random_color():

   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)

   return (r,g,b)



def Draw_tri():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/3
    for _ in range(3):
        tur.rt(angle)
        tur.fd(50)

def Draw_sq():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/4
    for _ in range(4):
        tur.rt(angle)
        tur.fd(50)

def Draw_pen():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/5
    for _ in range(5):
        tur.rt(angle)
        tur.fd(50)


def Draw_hex():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/6
    for _ in range(6):
        tur.rt(angle)
        tur.fd(50)


def Draw_hep():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/7
    for _ in range(7):
        tur.rt(angle)
        tur.fd(50)


def Draw_oct():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/8
    for _ in range(8):
        tur.rt(angle)
        tur.fd(50)


def Draw_non():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/9
    for _ in range(9):
        tur.rt(angle)
        tur.fd(50)


def Draw_dec():
    color = get_random_color()
    tur.pencolor(color)
    angle = 360/10
    for _ in range(10):
        tur.rt(angle)
        tur.fd(50)


Draw_tri()
Draw_sq()
Draw_pen()
Draw_hex()
Draw_hep()
Draw_oct()
Draw_non()
Draw_dec()
screen = Screen()
screen.colormode(255)
screen.exitonclick()
