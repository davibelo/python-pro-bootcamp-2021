import requests
from dotenv import load_dotenv
import os
import datetime as dt

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "davibelo"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

headers = {"X-USER-TOKEN": TOKEN}

today = dt.datetime.now()
# today = dt.datetime(year=2021, month=4, day=30)

# # registering...
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# # creating a new graph
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Running Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai"
# }
# # authentication using header
# response = requests.post(url=graph_endpoint, json=graph_config,
#                          headers=headers)
# print(response.text)

# creating a new pixel
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# creating a new pixel
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you run today?"),
}
response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data,
                         headers=headers)
print(response.text)

# # updating a pixel:
# update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "20"
# }
# response = requests.put(url=update_endpoint,
#                          json=new_pixel_data, headers=headers)
# print(response.text)

# # deleting a pixel
# delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
