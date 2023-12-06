import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tur = Turtle()
tur.shape("turtle")


def get_random_color():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   return (r,g,b)


circ = 0

for _ in range(100):

   if circ % 2 == 0:
      tur.begin_fill()
      tur.circle(50)
      tur.lt(11)
      color = get_random_color()
      tur.pencolor(color)
      tur.speed(100)
      tur.end_fill()
      circ += 1
   if circ % 2 != 0:
      tur.circle(50)
      circ += 1
      tur.lt(11)
      color = get_random_color()
      tur.pencolor(color)
      tur.speed(100)
      circ += 1





screen = Screen()
screen.colormode(255)
screen.exitonclick()
