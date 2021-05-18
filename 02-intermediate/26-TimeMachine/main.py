from bs4 import BeautifulSoup
import requests

# date = input("Type the date you want to come back (YYYY-MM-DD):")
date = "2010-12-09"

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

songs_tags = soup.find_all(name="span",
                           class_="chart-element__information__song")
artists_tags = soup.find_all(name="span",
                             class_="chart-element__information__artist")


songs = [song.getText() for song in songs_tags]
artists = [artist.getText() for artist in artists_tags]

print(songs)
print(artists)

