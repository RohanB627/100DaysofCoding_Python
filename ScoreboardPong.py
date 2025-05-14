from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score_pad1 = 0
        self.score_pad2 = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.create(self.score_pad1, (35,275))
        self.create(self.score_pad2, (-75,275))


    def create(self,pad,position):
        self.goto(position)
        self.write(arg=f"{pad}", move=False, font=("Courier", 70, "normal"))

    def update_score(self,pad,position):
        self.goto(position)
        self.write(arg=f"{pad}", move=False, font=("Courier", 70, "normal"))



