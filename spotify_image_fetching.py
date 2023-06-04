import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
from globals import current_song_name

load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


def fetch_album_image(song_name):
    # Create the Spotify client credentials manager
    client_credentials_manager = SpotifyClientCredentials(
        client_id=spotify_client_id, client_secret=spotify_client_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the track
    results = sp.search(q=song_name, type="track", limit=1)

    # Check if any tracks were found
    if (
        "tracks" in results
        and "items" in results["tracks"]
        and len(results["tracks"]["items"]) > 0
    ):
        track = results["tracks"]["items"][0]
        # Check if the track has album information
        if "album" in track:
            album = track["album"]
            # Check if the album has image information
            if "images" in album and len(album["images"]) > 0:
                # Get the URL of the first image (album cover)
                image_url = album["images"][0]["url"]
                return image_url

    return None
