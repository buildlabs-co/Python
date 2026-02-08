import random
from turtle import Turtle,Screen

screen = Screen()
is_race_on =False
screen.setup(width=500,height=400)
color=["red","orange","green","blue","purple","pink"]
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_pos[turtle_index])
    all_turtle.append(new_turtle)
user_bet = screen.textinput(title="place your bet",prompt="which turtle wins? pick a color:")


is_race_on =True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on =False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"win, the {winning_color} turtle is the winner!")
            else:
                print("you lose! the {winning_color} turtle is the winner!")
        speed=random.randint(1,10)
        turtle.forward(speed)





screen.exitonclick()