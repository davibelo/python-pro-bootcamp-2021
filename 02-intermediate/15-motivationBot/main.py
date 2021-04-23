from dotenv import load_dotenv
import os
import smtplib
import datetime as dt
import random


# loading constants
RELATIVE_PATH = "02-intermediate/15-motivationBot"
MY_EMAIL = "davibelo.bot@gmail.com"
load_dotenv(dotenv_path=f"{RELATIVE_PATH}/.env")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
print(MY_EMAIL_PASSWORD)

# getting today data
now = dt.datetime.now()
weekday = now.weekday()

# checking day of the week
if weekday == 4:
    # choosing a random motivation quote
    with open(f"{RELATIVE_PATH}/quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)

    # getting destination information
    name = "Davi Belo"
    email = "davibelo@gmail.com"

    # sending email with motivation
    print("sending email...")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Monday motivation!\n\nDear {name},\n\n{quote}\n\nHave a great week!\n\nDaviBot"
        )
    print("email sent!")
