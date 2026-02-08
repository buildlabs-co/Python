from turtle import Turtle,Screen,colormode
colormode(255)
import random

#import  colorgram
# Extract 6 colors from an image.
    # colors = colorgram.extract('paint.jpg', 20)
    #
    # rgb = []
    # for color in colors:
    #     r = color.rgb.r
    #     g = color.rgb.g
    #     b  = color.rgb.b
    #     new_rbg = (r,g,b)
    #     rgb.append(new_rbg)
    # print(rgb)
color_list = [(46, 92, 144), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16)]
t = Turtle()
t.speed("fast")
t.penup()
t.hideturtle()


def paint():
    for _ in range(10):
        rgb = random.choice(color_list)
        t.color(rgb)
        t.dot(20)
        t.forward(50)

def art():
    y = -150
    for _ in range(10):
        t.teleport(-300, y)
        paint()
        y += 50

art()

s = Screen()
s.exitonclick()

