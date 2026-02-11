from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my new_segment game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #DETECTING FOOD COLLISION
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #DETECTING WALL COLLISION
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False
    #DETECTING TAIL COLLISION
    for segment in snake.new_segment[1:]:
        if snake.head.distance(segment) <10:
            score.game_over()
            game_is_on = False













screen.exitonclick()