import spotipy
import pafy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# Set up Spotify client
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Set up Youtube API
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# def fetch_top_songs():
#     # Fetch the top songs from the Spotify API
#     playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
#     results = sp.playlist(playlist_id)
#     tracks = results["tracks"]["items"]
#     song_list = [
#         (track["track"]["name"], track["track"]["preview_url"]) for track in tracks
#     ]

#     # Filter out songs with None URL
#     song_list = [(song, url) for song, url in song_list if url is not None]

#     return song_list


def fetch_top_songs():
    # Fetch the top songs from the Spotify API
    playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]["items"]
    song_list = [
        (
            track["track"]["name"],
            track["track"]["artists"][0]["name"],
            track["track"]["preview_url"],
        )
        for track in tracks
    ]

    # Filter out songs with None URL
    song_list = [
        (song, artist, url) for song, artist, url in song_list if url is not None
    ]

    return song_list
