from tkinter import *
import math

from PIL.ImageStat import Global

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", font=(FONT_NAME, 35, "bold"), fill = "White")
    timer_label.config(text="Timer", fg = GREEN)
    tick_label.config(text = "")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg = RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg = PINK)
    elif reps%2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work Time")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        col_tick = []
        tick = "✔"
        for r in range(reps):
            if r%3 == 0:
                col_tick.append(tick)
                tick_label.config(text = tick*len(col_tick))
            else:
                pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text = "Timer", fg = GREEN, font=(FONT_NAME, 60, "bold"), bg=YELLOW, padx=-20)
timer_label.grid(column = 2, row=0)

button_start = Button(text = "Start", bg = YELLOW, borderwidth=0, highlightthickness=0, pady=5, command= start_timer)
button_start.grid(column = 0, row = 3)

button_reset = Button(text = "Reset", bg=YELLOW, borderwidth=0, highlightthickness=0, pady=5, command= reset_time)
button_reset.grid(column = 3, row = 3)

tick_label = Label(fg= GREEN, bg = YELLOW)
tick_label.grid(column = 2, row = 4)

canvas = Canvas(width= 200, height = 226, bg=YELLOW, highlightthickness=0, borderwidth=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", font=(FONT_NAME, 35, "bold"), fill = "White")
canvas.grid(column = 2, row = 2)



window.mainloop()