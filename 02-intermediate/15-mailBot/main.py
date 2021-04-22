from dotenv import load_dotenv
import os
import smtplib


MY_EMAIL = "davibelo.bot@gmail.com"
load_dotenv(dotenv_path="02-intermediate/15-mailBot/.env")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="davi.belo@outlook.com", 
                        msg="Subject:Hello!\n\nThis is the body of my email")

print("mail sent")
