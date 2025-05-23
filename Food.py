from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-230, 230)
        rand_y = random.randint(-230, 230)
        self.goto(rand_x, rand_y)