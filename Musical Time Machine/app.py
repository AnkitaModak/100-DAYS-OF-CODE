import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
spotify_client_id = config.SPOTIFY_CLIENT_ID
spotify_client_secret = config.SPOTIFY_CLIENT_SECRET
spotify_redirect_uri = "https://example.com"
spotify_username = config.SPOTIFY_USERNAME
date = input("WHich year do you want to travel to? Type the date in this format YYYY-MM-DD:")
#date= "2025-01-26"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
url = "https://www.billboard.com/charts/hot-100/2000-08-12/"
response = requests.get(url=url , headers=header)
soup = BeautifulSoup(response.text,"html.parser")
song_tag = soup.select("ul li ul li h3")
song_names = []
for song in song_tag:
    song_text = song.getText().strip()
    song_names.append(song_text)
# print(song_texts)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=spotify_redirect_uri,
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=spotify_username,
    )
)
user = sp.current_user()
user_id = user["id"]
print(user_id)
year = date.split("-")[0]
song_uris =[]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
