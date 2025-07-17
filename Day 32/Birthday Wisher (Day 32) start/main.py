import smtplib
import datetime as dt
import random

items = []

with open ("quotes.txt") as quote_file:
    for x in quote_file:
        items.append(x)

rand_quote = random.choice(items)
print(rand_quote)

now = dt.datetime.now()
year = now.year
week = now.weekday()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_day = days_of_week[week]




if week == "Thursday":
    my_email = "mangeykyo@gmail.com"
    password = "gkwj bvke jwuy tpdi"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs="martin.jeffrey44@gmail.com",
            msg= f"Subject: {current_day} Quote\n\n {rand_quote}"
        )
else:
    print("Pass")
