from turtle import Screen
from PongScreen import Window
from Padd import Paddle
from Ball import Ball
from ScoreboardPong import Scoreboard
import time

screen = Screen()


screen.setup(width=1000,height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



window = Window()
window.fence()




ball = Ball()
paddle_r = Paddle((400,40))
paddle_l = Paddle((-400,40))
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun= paddle_r.paddle_up, key="Up")
screen.onkey(fun= paddle_r.paddle_down, key= "Down")
screen.onkey(fun= paddle_l.paddle_up, key ="w")
screen.onkey(fun= paddle_l.paddle_down, key ="s")

x = 0.1




game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 330 or ball.ycor() <-330:
        ball.collision()

    if ball.distance(paddle_r) < 35 and ball.xcor() > 340 or ball.distance(paddle_l) < 35 and ball.xcor() < -300:
        ball.collision_paddle()
        x *=0.01


    if ball.xcor() >= 480:
        ball.goto(0,0)
        ball.move_speed = 0.1
        ball.x_move *=-1
        scoreboard.clear()
        scoreboard.score_pad2 += 1
        scoreboard.update_score(scoreboard.score_pad2, (-75,275))
        scoreboard.update_score(scoreboard.score_pad1, (35,275))
    elif ball.xcor() <= -480:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.x_move *= -1
        scoreboard.clear()
        scoreboard.score_pad1 += 1
        scoreboard.update_score(scoreboard.score_pad1, (35,275))
        scoreboard.update_score(scoreboard.score_pad2, (-75, 275))





screen.exitonclick()