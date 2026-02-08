#challenge 4
from turtle import Turtle,Screen,colormode
import random

colormode(255)
def ran_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rbg = (r,g,b)
    return rbg
tim = Turtle()
tim.width(9)
tim.speed("fast")

#colors = ["darkSlateBlue","slateBlue","lavender","indigo","mediumPurple","mediumOrchid","orchid","plum","thistle","violet","mediumVioletRed","violetRed","paleVioletRed","lightPink","pink","linen","rosyBrown"]
direction=[0,90,180,270]

for _ in range(300):
    tim.color(ran_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()