from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- SCRAPING BILLBOARD WEBSITE --- #

# date = input("Type the date you want to come back (YYYY-MM-DD):")
date = "2010-12-09"

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(BILLBOARD_URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

songs_tags = soup.find_all(name="span",
                           class_="chart-element__information__song")

PLAYLIST_SIZE = 30

song_names = [song.getText() for song in songs_tags[:PLAYLIST_SIZE]]
print(song_names)

# --- ACCESSING SPOTIFY WEB API --- #

# getting actual directory and making a rel path
REL_PATH = f"{os.path.dirname(__file__)}/"

# loading environment variables
load_dotenv(dotenv_path=f"{REL_PATH}.env")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://localhost"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                              client_secret=SPOTIFY_CLIENT_SECRET,
                              redirect_uri=REDIRECT_URI,
                              scope="playlist-modify-private"))
user_id = sp.current_user()["id"]

song_URIs = []
for song in song_names:
    results = sp.search(q=f"track:{song} year:{date[:4]}", limit=1, type="track")
    try:
        song_URIs.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        continue

print(song_URIs)

