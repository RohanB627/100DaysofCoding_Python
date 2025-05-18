import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()
car.cars_create()





screen.listen()
screen.onkey(fun=player.move, key="Up")

i = 0

game_is_on = True
while game_is_on:
    car.cars_move()
    time.sleep(car.speed)
    screen.update()
    i += 1

    for k in car.segment_car[0:]:
        if k.distance(player)<31:
            game_is_on = False
            scoreboard.game_over()

    if i%6 == 0:
        car.cars_create()

    if player.ycor() == 280:
        player.end()
        scoreboard.level += 1
        scoreboard.clear()
        scoreboard.update_score()
        car.speed*=0.5


screen.exitonclick()