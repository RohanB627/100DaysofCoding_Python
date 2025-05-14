from turtle import Turtle

# 400, 40
  # POS  = [(400,60), (400,50), (400,40), (400,30), (400,20), (400,10), (400,0), (400,-10), (400,-20), (400,-30)]
# POS_2 = [(-400,60), (-400,50), (-400,40), (-400,30), (-400,20), (-400,10), (-400,0), (-400,-10), (-400,-20), (-400,-30)]

class Paddle(Turtle):
    def __init__(self,p):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(p)
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def paddle_up(self):
        if self.ycor() < 300:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)




