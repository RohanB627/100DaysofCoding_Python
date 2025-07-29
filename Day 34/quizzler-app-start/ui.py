from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,q: QuizBrain):
        self.quiz = q

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, bg = THEME_COLOR)
        self.canvas = Canvas(height= 250, width = 300, highlightthickness=0, bg= "White")
        self.canvas.grid(row = 1, column=0, columnspan=2,  padx=20, pady= 20)

        # Buttons
        self.true = PhotoImage(file = "/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 34/quizzler-app-start/images/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, borderwidth=0, command= self.true_pressed)
        self.true_button.grid(row = 2, column = 0)
        self.false = PhotoImage(file = "/Users/rohanbhagchandani/Desktop/100DaysofCoding 2/Day 34/quizzler-app-start/images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, borderwidth=0, command= self.false_pressed)
        self.false_button.grid(row=2, column=1, pady = 20)

        # Text
        self.score_display = Label(text= f"Score: 0", font=("Ariel", 20, "bold"), bg= THEME_COLOR)
        self.score_display.grid(row = 0, column = 1)
        self.question_text = self.canvas.create_text(150, 125, text = "......", font = ("Arial", 20, "italic"), fill = "Green", width= 250)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_display.config(text = f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text = f"{q_text}", fill = "Black")
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz.")
            self.true_button.config(state = "disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="White")

    def true_pressed(self):
        self.true_button = "True"
        self.give_feedback(self.quiz.check_answer(self.true_button))

    def false_pressed(self):
        self.false_button = "False"
        self.give_feedback(self.quiz.check_answer(self.false_button))

    def after_delay(self):
        self.get_next_question()
        self.canvas.config(bg="White")

    def give_feedback(self, is_right):
        self.window.after(1000,self.after_delay)
        if is_right is True:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")









