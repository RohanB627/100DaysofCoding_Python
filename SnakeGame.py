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
scoreboard = Scoreboard()
score = 0



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.clear()
        scoreboard.score += 1
        food.refresh()
        snake.extend()
        scoreboard.update_score()


    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_on = False
        scoreboard.game_end()

    for i in snake.items[1:]:
        if snake.head.distance(i) <10:
            game_on = False
            scoreboard.game_end()

    print(snake.items[2:])










screen.exitonclick()
