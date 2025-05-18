from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=270)
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def update_score(self):
       self.write(f"Level: {self.level}", move=False, font=FONT)

    def game_over(self):
        self.color("Black")
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Courier", 24, "normal"))

