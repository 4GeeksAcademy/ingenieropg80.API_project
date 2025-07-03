import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

ml_uri = 'spotify:artist:3muH0fOWJZ2SaxK3agdOMD'
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))

results = sp.artist_top_tracks(ml_uri)

songs = []
for track in results['tracks'][:10]:
    song_info = {
        'name': track['name'],
        'duration_ms': track['duration_ms'],
        'popularity': track['popularity']
    }
    songs.append(song_info)
df = pd.DataFrame(songs)

df_sorted = df.sort_values(by="popularity", ascending=False)
top_3 = df_sorted.head(3)
print(df) #intento separar con \n
print(top_3)


plt.scatter(df['duration_ms'], df['popularity'])
plt.xlabel('Duración (ms)')
plt.ylabel('Popularidad')
plt.title('Popularidad vs duración')
plt.show()
#plt.show(block=True)

