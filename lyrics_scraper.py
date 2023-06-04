import requests
from lxml import html


def scrape_lyrics(artist, song):
    # Format the artist and song names for the URL
    artist_formatted = artist.lower().replace(" ", "")
    song_formatted = song.lower().replace(" ", "")

    # Build the lyrics URL
    lyrics_url = (
        f"https://www.azlyrics.com/lyrics/{artist_formatted}/{song_formatted}.html"
    )

    # Send a GET request to the lyrics page
    response = requests.get(lyrics_url)

    # Parse the HTML content
    tree = html.fromstring(response.content)

    # Extract the lyrics using the XPath
    lyrics = tree.xpath("/html/body/div[2]/div[2]/div[2]/div[5]/text()")

    # Join the extracted lyrics into a single string
    lyrics_text = "\n".join(lyrics)

    # Return the lyrics
    return lyrics_text
