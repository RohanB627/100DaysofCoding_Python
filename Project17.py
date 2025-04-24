import random
from turtle import Turtle, Screen

#
# color = colorgram.extract('image.jpg', 88)
#
# colors = []
#
# for x in color:
#     m = x.rgb
#     k = (m[0],m[1],m[2])
#     colors.append(k)
#
# print(colors)

color_list = [(237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188),
      (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149),
      (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16),
      (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155),
      (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224),
      (36, 243, 159), (6, 81, 115), (11, 55, 248)]


timmy = Turtle()
Screen().colormode(255)
timmy.penup()


def row():
        timmy.speed(2)
        timmy.forward(50)
        timmy.dot(20, random.choice(color_list))


x = -300
y = -250
timmy.setpos(x,y)

for x in range(1,101):
    row()
    if x % 10 == 0:
        x = -300
        y += 50
        timmy.setpos(x, y)

screen = Screen()
screen.exitonclick()



#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r,g,b
#
# n = 10
#
# print(random_color())
# print(type(random_color()))
# Screen().colormode(255)
# direction = 0
# for _ in range(80):
#     timmy.speed(30)
#     timmy.pencolor(random_color())
#     timmy.circle(100)
#     direction +=5
#     timmy.setheading(direction)
#     # timmy.forward(25)


# timmy.color("red")
#
# for _ in range(3):
#     # triangle
#     timmy.forward(100)
#     timmy.right(120)
#     timmy.color("red")
#
# #     square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.color("blue")
#
# # pentagon
# for _ in range(5):
#     timmy.forward(100)
#     timmy.right(72)
#     timmy.color("green")
#
# # heptagon
# for _ in range(7):
#     timmy.forward(100)
#     timmy.right(51.43)
#     timmy.color("yellow")
#
# # octagon
# for _ in range(8):
#     timmy.forward(100)
#     timmy.right(45)
#     timmy.color("orange")
#
#
# # nonagon
# for _ in range(9):
#     timmy.forward(100)
#     timmy.right(40)
#     timmy.color("black")
#
# # decagon
# for _ in range(10):
#     timmy.forward(100)
#     timmy.right(36)
#     timmy.color("magenta")


