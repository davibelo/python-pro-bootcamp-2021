import os
import requests
from dotenv import load_dotenv

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

SHEET_NAME = "users"
SHEET_NAME_SINGULAR = "user"
sheety_key = os.getenv('SHEETY_APIKEY')
sheety_headers = {
    "Authorization": sheety_key,
    "Content-Type": "application/json"
}
sheety_endpoint = "https://api.sheety.co/3955488f8ee023601d308d21b9639dd3/flightDeals"

first_name = input("type your first name: ")
last_name = input("type your last name: ")
email = input("type your email: ")
email_confirmation = input("confirm your email: ")
if email == email_confirmation:
    json_body = {
        SHEET_NAME_SINGULAR: {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(url=f"{sheety_endpoint}/{SHEET_NAME}",
                             headers=sheety_headers,
                             json=json_body)
    response.raise_for_status()
    print("Welcome to the club!")
