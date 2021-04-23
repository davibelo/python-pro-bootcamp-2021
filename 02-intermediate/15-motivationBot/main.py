from dotenv import load_dotenv
import pandas as pd
import datetime as dt
import os
import smtplib
import random

# loading constants
RELATIVE_PATH = "02-intermediate/15-motivationBot"
MY_EMAIL = "davibelo.bot@gmail.com"
load_dotenv(dotenv_path=f"{RELATIVE_PATH}/.env")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")

# getting today data
now = dt.datetime.now()
weekday = now.weekday()

# checking day of the week
if weekday == 4:
    # choosing a random motivation quote
    with open(f"{RELATIVE_PATH}/quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)

    # getting contacts information
    df = pd.read_csv(f"{RELATIVE_PATH}/emails_test.csv")
        
    # looping through contacts data frame
    for (index, row) in df.iterrows():
        dest_name = row["name"]
        dest_email = row["email"]    
    
        # sending email with motivation
        print("sending email...")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=dest_email,
                msg=f"Subject:Monday motivation!\n\nDear {dest_name},\n\n{quote}\n\nHave a great week!\n\nDaviBot"
            )
        print("email sent!")
