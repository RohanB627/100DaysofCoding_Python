from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 40


class CarManager:
    def __init__(self):
        self.speed = 0.1
        self.segment_car = []

    def cars_create(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(x=300, y=random.randint(-250, 250))
        car.setheading(180)
        self.segment_car.append(car)

    def cars_move(self):
        for r in self.segment_car:
            r.forward(STARTING_MOVE_DISTANCE)










