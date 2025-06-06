# def add(*addition):
#     k = 0
#     for n in addition:
#       k+=n
#     return k
#
# print(add(2,3,2,1,3,4,6,7,8,9))
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 300,height = 100)



convert_result = 0


def click():
    item = value.get()
    con_item = float(item)*1.60934
    converted.config(text = f"  {con_item}")


mile = Label(text = "Miles", font=("Arial", 24, "bold"))
mile.grid(column = 6, row = 1)


# input_var = StringVar()
value = Entry(width = 5)
value.grid(column = 5, row = 1)

another = Label(text = "is equal to", font=("Arial", 24, "bold"))
another.grid(column = 4, row = 2)

converted = Label(text = f"0", font=("Arial", 24, "bold"))
converted.grid(column = 5, row = 2)

km = Label(text = "KM", font=("Arial", 24, "bold"))
km.grid(column = 6, row = 2)

button = Button(text = "Calculate", command = click)
button.grid(column = 5, row = 3)













window.mainloop()
