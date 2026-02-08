from turtle import Turtle ,Screen
import random

tim = Turtle()
tim.shape("turtle")
#challenge 1 :  SQUARE

for _ in range(4):
    tim.forward(50)
    tim.right(90)

# timmy.forward(50)
# timmy.right(90)
# timmy.forward(50)
# timmy.right(90)
# timmy.forward(50)

#challenge 2: DASHED LINES
# for _ in range(20):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")
#     tim.right(12.221)
#
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(5)
    tim.pendown()

#challenge 3:
color = ["dark slate blue","slate blue","lavender","indigo","medium purple","medium orchid","orchid","plum","thistle","violet","medium violet red","violet red","pale violet red","light pink","pink","linen","rosy brown"]

def draw_shape(num_of_sides):
    angle=(360/num_of_sides)
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape in range(3,11):
    tim.color(random.choice(color))
    draw_shape(shape)

# for _ in range(3):
#     tim.right(360/3)
#     tim.forward(100)
#
# for _ in range(4):
#     tim.color("red")
#     tim.right(360/4)
#     tim.forward(100)
#
# for _ in range(5):
#     tim.color("blue")
#     tim.right(360/5)
#     tim.forward(100)
#
# for _ in range(6):
#     tim.color("orange")
#     tim.right(360/6)
#     tim.forward(100)
#
# for _ in range(7):
#     tim.color("green")
#     tim.right(360/7)
#     tim.forward(100)
#
# for _ in range(8):
#     tim.color("violet")
#     tim.right(360/8)
#     tim.forward(100)
#
# for _ in range(9):
#     tim.color("brown")
#     tim.right(360/9)
#     tim.forward(100)
#
# for _ in range(10):
#     tim.color("pink")
#     tim.right(360/10)
#     tim.forward(100)

screen = Screen()
screen.exitonclick()