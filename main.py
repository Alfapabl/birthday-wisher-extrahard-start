##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas as pd
import random
my_email = "primefreetest@gmail.com"
password = "palos009"

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
day_of_week = now.day
month = now.month
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for i in df.index:
    if day_of_week == df.day[i] and month == df.month[i]:
        random_letter = random.choice(letters)
        replaced_text = df.name[i]
        search_text = "[NAME]"
        with open(f"letter_templates\{random_letter}", "r") as file:
            data = file.read()
            data = data.replace(search_text, replaced_text)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=df.email,
                                msg=f"Subject:Happy Birthday\n\n{data}")


