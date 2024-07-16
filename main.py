from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("yellow")
screen.title("Snake up!")
screen.tracer(0)

slizzy = Snake()
foodie = Food()
scorer = ScoreBoard()

screen.listen()
screen.onkey(slizzy.up, "Up")
screen.onkey(slizzy.down, "Down")
screen.onkey(slizzy.left, "Left")
screen.onkey(slizzy.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    slizzy.move()
    if slizzy.head.distance(foodie) < 15:
        foodie.another_food()
        slizzy.extend()
        scorer.increase_score()

    if slizzy.head.xcor() > 280 or slizzy.head.xcor() < -280 or slizzy.head.ycor() > 280 or slizzy.head.ycor() < -280:
        scorer.reset()
        slizzy.reset()

    for taipan in slizzy.snakes[1:]:
        if slizzy.head.distance(taipan) < 10:
            scorer.reset()
            slizzy.reset()

screen.exitonclick()
