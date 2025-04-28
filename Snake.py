from turtle import Turtle

Pos = [(0,0),(-20,0),(-40,0)]
M_Dis = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.items = []
        self.create()
        self.head = self.items[0]
        self.move()

    def create(self):
        for p in Pos:
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(p)
            self.items.append(new_turtle)

    def move(self):
        for k in range(len(self.items) -1 ,0,-1):
            seg_3x = self.items[k-1].xcor()
            seg_3y = self.items[k-1].ycor()
            self.items[k].goto(seg_3x,seg_3y)
        self.items[0].forward(M_Dis)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

