##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
import random

items = []

now = dt.datetime.now()
month = now.month
day = now.day

rand_number = random.randint(1,3)
print(rand_number)


with open (f"letter_templates/letter_{rand_number}.txt") as bday_letter:
    read = bday_letter.read()
    items.append(read)



df = pd.read_csv("birthdays.csv")
for index,row in df.iterrows():
    if row["month"] and row["day"] == day:
        amend_letter = [x.replace("[NAME]", row["name"]) for x in items]
        items = amend_letter
        for x in items:
                my_email = "mangeykyo@gmail.com"
                password = "gkwjbvkejwuytpdi"

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs= row["email"],
                        msg=f"Subject: Happy Birthday\n\n {x}"
                    )





