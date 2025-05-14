from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01


    def create_ball(self):
        self.penup()
        self.shape("square")
        self.shapesize(1)
        self.color("blue")

    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x + self.x_move
        new_y = current_y + self.y_move
        self.goto(new_x,new_y)

    def collision(self):
        self.y_move *= -1

    def collision_paddle(self):
        self.x_move *= -1
        self.move_speed *=0.9








