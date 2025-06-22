from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    nr_letters = [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    nr_symbols = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    nr_numbers = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, string= f"{password}")
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as dat_1:
            data = json.load(dat_1)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message = "No Data File found")
    else:
        if website in data:
            messagebox.showinfo(title = f"{website}", message = f"Email: {data[website]['email']}\n Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title = "Error", message = f"No details for the {website}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_ret = web_entry.get()
    email_user_ret = email_user_entry.get()
    pass_ret = pass_entry.get()
    new_data = {
        web_ret: {
            "email": email_user_ret,
            "password": pass_ret
        }
    }

    if len(web_ret) == 0 or len(pass_ret) == 0:
        messagebox.showinfo(title="Details", message="Please check - some details are missing")
    else:
        try:
            with open("data.json", "r") as dat:
                data = json.load(dat)
                data.update(new_data)
            with open("data.json", "w") as dat:
                json.dump(data, dat, indent = 3)
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
        except FileNotFoundError:
            with open("data.json", "w") as dat:
                json.dump(new_data, dat, indent = 3)
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width= 200, height = 200)
pwd_img = PhotoImage(file="logo.png")
canvas.create_image(125,100, image= pwd_img)
canvas.grid(column = 1, row = 0)

web_label = Label(text = "Website: ")
web_label.grid(column = 0, row = 1)

web_entry = Entry(width = 21)
web_entry.grid(column = 1,row = 1)
web_entry.focus()

search = Button(text ="Search", width = 13, pady = 2, command = find_password)
search.grid(column = 2, row = 1)

email_user_label = Label(text = "Email/Username: ")
email_user_label.grid(column = 0, row = 2)

email_user_entry = Entry(width = 37)
email_user_entry.grid(column = 1, columnspan=2, row = 2)
email_user_entry.insert(0,"rohan.bhagchandani25@gmail.com")

pass_label = Label(text = "Password: ")
pass_label.grid(column = 0, row = 3)

pass_entry = Entry(width = 21)
pass_entry.grid(column = 1, row = 3)

pass_gen_button = Button(text ="Generate Password", width = 13, pady = 2, command=generate_pass)
pass_gen_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width=35, pady= 0, command = save)
add_button.grid(column = 1, columnspan=2 , row = 4)


window.mainloop()