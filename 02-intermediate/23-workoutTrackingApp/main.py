import requests
from dotenv import load_dotenv
import os
import datetime as dt

GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 178
AGE = 39

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

NUTRITION_APPID = os.getenv("NUTRITION_APPID")
NUTRITION_APIKEY = os.getenv("NUTRITION_APIKEY")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITION_APPID,
    "x-app-key": NUTRITION_APIKEY,
    "Content-Type": "application/json",
}

body = {
    "query": input("Type the exercise"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, body=body, headers=headers)
print(response)