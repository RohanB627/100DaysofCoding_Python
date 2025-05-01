from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.goto(-55, 275)
        self.color("White")
        self.write(arg=f"Score: {self.score}", move=False, font=("Courier", 20, "normal"))

    def update_score(self):
        self.write(arg=f"Score: {self.score}", move=False, font=("Courier", 20, "normal"))

    def game_end(self):
        self.color("White")
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align = "center", font=("Courier", 20, "normal"))
