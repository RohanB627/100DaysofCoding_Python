from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.goto(-55, 275)
        self.color("White")
        self.write(arg=f"Score: {self.score}", move=False, font=("Courier", 20, "normal"))