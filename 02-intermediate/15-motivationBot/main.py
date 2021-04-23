from dotenv import load_dotenv
import os
import smtplib
import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("02-intermediate/15-mailBot/quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)

load_dotenv(dotenv_path="02-intermediate/15-mailBot/.env")
MY_EMAIL = "davibelo.bot@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="davi.belo@outlook.com",
        msg=f"Subject:Monday motivation!\n\n{quote}"
    )
