# import colorgram as cg
import random as r
import turtle as t
# rgb_colors = []
# colors = cg.extract('img.jpg', 30)
#
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#
# print(rgb_colors)
t.colormode(255)
turt = t.Turtle()
turt.speed(100)
turt.penup()
turt.hideturtle()

color_list = [(31, 102, 156), (149, 23, 55), (224, 158, 51), (165, 64, 109), (217, 212, 50), (170, 72, 47), (42, 104, 61), (205, 137, 175), (96, 170, 115), (55, 37, 44), (39, 54, 121), (34, 36, 72), (22, 68, 58), (231, 188, 21), (56, 80, 48), (234, 241, 237), (210, 100, 48), (244, 218, 7), (161, 101, 153), (47, 149, 185), (127, 160, 186), (217, 177, 190), (109, 120, 159), (94, 154, 115), (180, 186, 212), (172, 203, 181), (226, 177, 166)]

turt.setheading(225)
turt.fd(250)
turt.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    turt.dot(20, r.choice(color_list))
    turt.fd(50)
    if dot_count % 10 == 0:
        turt.setheading(90)
        turt.fd(50)
        turt.setheading(180)
        turt.fd(500)
        turt.setheading(0)


screen = t.Screen()
screen.exitonclick()