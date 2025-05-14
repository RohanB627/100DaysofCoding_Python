from turtle import Turtle

class Window(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 350)
        self.hideturtle()
        self.setheading(270)
        self.color("white")
        self.pensize(6)

    def fence(self):
        for _ in range(12):
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()



