from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
score1 = Scoreboard()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
rand_food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score1.gameover()
    if snake.head.distance(rand_food) < 15:
        score1.increasescore()
        rand_food.refresh()
        snake.extend()
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            score1.gameover()
screen.exitonclick()
