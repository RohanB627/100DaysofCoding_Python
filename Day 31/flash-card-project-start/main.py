from tkinter import *

import pandas
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"
words = None
timer = None


# ---------------------- CSV reader and random word generator ------------------
try:
    read_new = pd.read_csv("/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 31/flash-card-project-start/words_to_learn.csv")
except FileNotFoundError:
    read = pd.read_csv("/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 31/flash-card-project-start/data/french_words.csv")
    read_df_to_dic = read.to_dict(orient = "records")
else:
    read_df_to_dic = read_new.to_dict(orient = "records")

def left_rand_word():
    global words
    global timer
    if timer is not None:
        window.after_cancel(timer)

    rand_word_li = random.choice(read_df_to_dic)
    words = rand_word_li
    pol_text = words['French']
    canvas.itemconfig(current_image, image=front_image)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(lang_pol_eng, text=f"{pol_text}", fill="Black")

    timer = window.after(3000, func=eng_word)


def right_rand_word():
    read_df_to_dic.remove(words)
    data = pandas.DataFrame(read_df_to_dic)
    data.to_csv("words_to_learn.csv", index = False)


    left_rand_word()


def eng_word():
    global words
    canvas.itemconfig(current_image, image=new_image)
    canvas.itemconfig(title, text = "English", fill = "White")
    canvas.itemconfig(lang_pol_eng, text=f"{words['English']}", fill = "White")



# ------------------------------------- UI -------------------------------------
window = Tk()
window.title("Flashy")
window.config(pady = 50, padx=50, bg = BACKGROUND_COLOR)


canvas = Canvas(height = 526, width= 800, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file = "/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 31/flash-card-project-start/images/card_front.png")
new_image = PhotoImage(file="/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 31/flash-card-project-start/images/card_back.png")
current_image = canvas.create_image(400,253,image= front_image)
canvas.grid(column = 0, row = 0, columnspan=2)

tick_box = PhotoImage(file = "/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 31/flash-card-project-start/images/right.png")
tick_box_button = Button(image=tick_box, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command = right_rand_word)
tick_box_button.grid(column = 1, row = 2)

wrong_box = PhotoImage(file = "/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 31/flash-card-project-start/images/wrong.png")
wrong_box_button = Button(image=wrong_box, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command = left_rand_word)
wrong_box_button.grid(column = 0, row = 2)

lang = canvas
title = lang.create_text(400,150, text = "....", font=("Ariel", 40, "italic"), fill ="Black")
lang.grid(column = 0, row = 0, columnspan= 2)

lang_word = canvas
lang_pol_eng = lang_word.create_text(400,263, text = "....", font=("Ariel", 60, "bold"), fill ="Black")
lang_word.grid(column = 0, row = 1, columnspan= 2)


left_rand_word()












window.mainloop()
