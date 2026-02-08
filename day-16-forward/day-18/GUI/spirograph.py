from turtle import Turtle,Screen,colormode
import random
colormode(255)
def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rbg = (r, g, b)
    return rbg

timy = Turtle()
timy.speed("fastest")
timy.shape("classic")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timy.color(ran_color())
        timy.circle(100)
        timy.setheading(timy.heading()+ size_of_gap)

draw_spirograph(5)
screeny = Screen()
screeny.exitonclick()