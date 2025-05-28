import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)

name = turtle.Turtle()
name.color("Black")
name.penup()
name.hideturtle()

correct_ans = []
learn = []
def check_answer(n):
    if n in data["state"].values:
        return True
    return None



game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{len(correct_ans)}/50", prompt="What's another state's name?").title()
    if check_answer(answer_state):
        correct_ans.append(answer_state)
        x = data[data.state == f"{answer_state}"].values[0][1]
        y = data[data.state == f"{answer_state}"].values[0][2]
        name.goto(x, y)
        name.write(arg=f"{answer_state}", move=False, font=("Courier", 10, "normal"))
        print(name.pos())
    if len(correct_ans) == 50:
        name.clear()
        name.home()
        name.write(arg="You got it!\n Game Over! ", move=False, font=("Courier", 10, "normal"))
        game_on = False
    elif answer_state == "Exit":
        cov_list = data["state"].values.tolist()
        for r in cov_list:
            if r not in correct_ans:
                learn.append(r)
        learn_states = pandas.DataFrame(learn)
        learn_states.to_csv("Learn")
        break

screen.mainloop()