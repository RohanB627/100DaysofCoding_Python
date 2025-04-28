from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()
food = Food()



score = 0
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        scoreboard.clear()
        food.refresh()

scoreboard = Scoreboard()








screen.exitonclick()