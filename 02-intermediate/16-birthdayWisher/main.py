from dotenv import load_dotenv
import os
import pandas as pd
import datetime as dt
import random
import smtplib

# Exercise
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

# constants
PLACEHOLDER = "[NAME]"
MY_EMAIL = "davibelo.bot@gmail.com"
RELATIVE_PATH = "02-intermediate/16-birthdayWisher"

# loading email password from .env file
load_dotenv(dotenv_path=f"{RELATIVE_PATH}/.env")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# reading birthdays from csv
df = pd.read_csv(f"{RELATIVE_PATH}/birthdays.csv")

# getting today information
now = dt.datetime.now()
today_tuple = (now.month, now.day)

# looping through each person on data frame
for (index, row) in df.iterrows():
    # checking if there is a birthday person today
    if (row.month, row.day) == today_tuple:

        # getting birthday person data
        name = row["name"]
        email = row["email"]

        # choosing a random letter
        letter_indexes = (1, 2, 3)
        letter_num = random.choice(letter_indexes)
        letter_path = f"{RELATIVE_PATH}/letter_templates/letter_{letter_num}.txt"

        # prepare letter
        with open(letter_path) as letter_file:
            letter_contents = letter_file.read()
            letter_final = letter_contents.replace(PLACEHOLDER, name)

        # send email with final letter
        print("sending email...")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{letter_final}"
            )
        print("email sent!")
