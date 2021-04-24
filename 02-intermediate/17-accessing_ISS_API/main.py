import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code == 404:
#     raise Exception("That resource does not exist")
# if response.status_code == 401:
#     raise Exception("You are not authorized to access this resource")

# instead of above code, just use:
response.raise_for_status()


print(f"header:{response.headers}")
print(f"text:{response.text}")

# json method process json responses directly
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)