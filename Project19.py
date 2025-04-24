import random
from turtle import Turtle, Screen

def turt(user):
    user = Turtle(shape="turtle")
    user.color(random.choice(colors))
    user.penup()

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -100

for _ in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x,y)
    new_turtle.color(colors[_])
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >=230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! the winning turtle is {winning_color}")
            else:
                print(f"You've lost! the winning turtle is {winning_color}")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)







# lim = Turtle(shape="turtle")
# lim.color(colors[1])
# lim.penup()
# lim.goto(x=-230, y=-50)
#
# kim = Turtle(shape="turtle")
# kim.color(colors[2])
# kim.penup()
# kim.goto(x=-230, y=0)
#
# pim = Turtle(shape="turtle")
# pim.color(colors[3])
# pim.penup()
# pim.goto(x=-230, y=50)
#
# sim = Turtle(shape="turtle")
# sim.color(colors[4])
# sim.penup()
# sim.goto(x=-230, y=100)
#
# fim = Turtle(shape="turtle")
# fim.color(colors[5])
# fim.penup()
# fim.goto(x=-230, y=150)





screen.exitonclick()