import turtle
from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]

turtle.colormode(255)
tur = Turtle()
tur.shape("turtle")
tur.color("purple")


def get_random_color():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   return (r,g,b)


thick = 1


for _ in range(200):
   tur.fd(30)
   color = get_random_color()
   tur.pencolor(color)
   tur.pensize(thick)
   thick += 1
   tur.speed(random.randint(1,11))
   tur.setheading(random.randint(0,360))


screen = Screen()
screen.colormode(255)
screen.exitonclick()
