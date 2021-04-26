from datetime import datetime, timezone
import requests
from dotenv import load_dotenv
import smtplib
import os
import time


# ---- CONSTANTS ---- #


MY_LAT = -8.0584933
MY_LNG = -34.8848193

REL_PATH = "02-intermediate/17-ISSreminder/"
MY_EMAIL = "davibelo.bot@gmail.com"
load_dotenv(dotenv_path=f"{REL_PATH}.env")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
DEST_EMAIL = "davibelo@gmail.com"


# ---- FUNCTIONS ---- #


def is_iss_overhead():
    """ checks if iss is overhead"""

    # accessing ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    # getting ISS position
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    else:
        return False


def is_night():
    "check if it is night locally"

    # organizing parametets to use on sunrise sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    # getting data on sunrise sunset API
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # getting local time sunrise and sunset hour in UTC
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # getting current time in UTC
    now_hour = datetime.now(timezone.utc).hour

    # checking if it is dark (considering 1 hour of twilight)
    if now_hour >= sunset_hour+1 or now_hour <= sunrise_hour-1:
        return True
    else:
        return False


def send_email():
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=DEST_EMAIL,
            msg=f"Subject:ISS ON SIGHT!\n\nLook Up, ISS is passing overhead\n\nRegards\nDaviBot"
        )
    print(f"email sent to {DEST_EMAIL}!")


# ---- MAIN LOOP ---- #


while True:    
    print("checking if ISS is on sight...")
    if is_iss_overhead() and is_night():
        send_email()
    time.sleep(60)
