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

# exercise API
NUTRITIONIX_APPID = os.getenv("NUTRITIONIX_APPID")
NUTRITIONIX_APIKEY = os.getenv("NUTRITIONIX_APIKEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APPID,
    "x-app-key": NUTRITIONIX_APIKEY,
    "Content-Type": "application/json",
}
exercise_data = {
    "query": "2 hour cycling",
    # "query": input("Type the exercise: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=NUTRITIONIX_ENDPOINT,
                         headers=NUTRITIONIX_HEADERS,
                         json=exercise_data)
exercise_response = response.json()["exercises"][0]
exercise_name = exercise_response["name"]
exercise_duration = exercise_response["duration_min"]
exercise_calories = exercise_response["nf_calories"]

today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%X")

# sheet write API
SHEETY_API_ENDPOINT = "https://api.sheety.co/3955488f8ee023601d308d21b9639dd3/myWorkouts/home"
SHEETY_APIKEY = os.getenv("SHEETY_APIKEY")
SHEETY_HEADERS = {
    "Authorization": SHEETY_APIKEY,
    "Content-Type": "application/json"
}
sheet_data = {
    "home": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories,
    }
}
response = requests.post(url=SHEETY_API_ENDPOINT,
                         headers=SHEETY_HEADERS,
                         json=sheet_data)
print(response.text)