from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

PLAYLIST_SIZE = 30
DATE = "2012-12-09"

# --- SCRAPING BILLBOARD WEBSITE --- #

print("getting song names...")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{DATE}"

response = requests.get(BILLBOARD_URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

songs_tags = soup.find_all(name="span",
                           class_="chart-element__information__song")

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

# querying musics
print("looking for musics...")
song_URIs = []
for song in song_names:
    results = sp.search(q=f"track:{song} year:{DATE[:4]}",
                        limit=1,
                        type="track")
    try:
        song_URIs.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        continue

# print(song_URIs)

# creating a playlist
print("creating a playlist...")
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id,
                                       name=f"Billboard {DATE}",
                                       public=False,
                                       collaborative=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_URIs, position=None)

