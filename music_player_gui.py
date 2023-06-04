from tkinter import *
import spotify_image_fetching
from PIL import Image, ImageTk
from io import BytesIO
from urllib.request import urlopen
import spotify_api_handler
import lyrics_scraper
import pygame
import requests
import os

current_image = None

# Create the main window for our application
root = Tk()
root.geometry("750x540")
root.title("Music Player")

# Create frames for the song image and the song list and control buttons
left_frame = Frame(root)
left_frame.grid(row=0, column=0, sticky="nsew")

separator = Frame(root, width=2, bg="black")
separator.grid(row=0, column=1, sticky="ns")

right_frame = Frame(root)
right_frame.grid(row=0, column=2, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Create a placeholder for the song image in the left frame
image = Image.open("image_placeholder.png")
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
song_image = Label(left_frame, image=photo)
song_image.pack()


def update_song_image(image_url):
    global current_image

    # Open the image from the URL
    image_data = urlopen(image_url).read()
    image = Image.open(BytesIO(image_data))

    # Resize the image
    image = image.resize((200, 200), Image.ANTIALIAS)

    # Create a PhotoImage object from the Image object
    current_image = ImageTk.PhotoImage(image)

    # Update the song image label
    song_image.config(image=current_image)
    song_image.image = current_image  # Keep a reference to prevent garbage collection


# Create a placeholder for the song list in the right frame
listbox = Listbox(right_frame)
listbox.pack(fill=BOTH, expand=True)

# Set the focus on the listbox
listbox.focus_set()


# Define the function to download a song
def download_song(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)


# Initialize pygame mixer
pygame.mixer.init()

# Fetch the top songs from the Spotify API
song_url_list = spotify_api_handler.fetch_top_songs()
song_list = song_url_list

# Add the songs to the listbox
for song, artist, url in song_list:
    listbox.insert(END, song)


# Initialize the current song index
current_song_index = 0


# Define the function to stop the current song
def stop_song():
    pygame.mixer.music.stop()


# Define the function to play a song
def play_song():
    selected_song_index = listbox.curselection()[
        0
    ]  # Get the index of the selected song
    selected_song = song_list[selected_song_index]  # Get the selected song and URL
    song_name, artist, song_url = selected_song

    # Download the song
    file_path = f"{song_name}.mp3"
    download_song(song_url, file_path)

    # Fetch the album image
    album_image_url = spotify_image_fetching.fetch_album_image(song_name)

    # Update the song image
    update_song_image(album_image_url)

    # Play the downloaded song
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the song to finish playing
    pygame.mixer.music.get_busy()
    while pygame.mixer.music.get_busy():
        root.update()

    # Delete the downloaded file
    os.remove(file_path)

    # Remove the played song from the listbox
    listbox.delete(selected_song_index)


# Define the function to play the next song
def play_next_song():
    selected_song_index = listbox.curselection()[
        0
    ]  # Get the index of the selected song
    next_song_index = (selected_song_index + 1) % len(
        song_list
    )  # Calculate the index of the next song
    listbox.selection_clear(selected_song_index)  # Clear the selection
    listbox.selection_set(next_song_index)  # Set the selection to the next song
    listbox.activate(next_song_index)  # Activate the next song in the listbox
    listbox.see(next_song_index)  # Scroll the listbox to show the next song
    play_song()


# Define the function to play the previous song
def play_previous_song():
    selected_song_index = listbox.curselection()[
        0
    ]  # Get the index of the selected song
    previous_song_index = (selected_song_index - 1) % len(
        song_list
    )  # Calculate the index of the previous song
    listbox.selection_clear(selected_song_index)  # Clear the selection
    listbox.selection_set(previous_song_index)  # Set the selection to the previous song
    listbox.activate(previous_song_index)  # Activate the previous song in the listbox
    listbox.see(previous_song_index)  # Scroll the listbox to show the previous song
    play_song()


# Create the control buttons
prev_button = Button(left_frame, text="Prev", command=play_previous_song)
prev_button.pack()

stop_button = Button(left_frame, text="Stop", command=stop_song)
stop_button.pack()

play_button = Button(left_frame, text="Play", command=play_song)
play_button.pack()

next_button = Button(left_frame, text="Next", command=play_next_song)
next_button.pack()

# Create a new frame for the lyrics scraper
lyrics_frame = Frame(right_frame)
lyrics_frame.pack(fill=BOTH, expand=True)

# Add a label and text area for displaying the lyrics
lyrics_label = Label(lyrics_frame, text="Lyrics:")
lyrics_label.pack()

lyrics_text = Text(lyrics_frame)
lyrics_text.pack(fill=BOTH, expand=True)


# Function to scrape lyrics
def fetch_lyrics():
    selected_song_index = listbox.curselection()[0]
    selected_song = song_list[selected_song_index]
    song_name, artist, song_url = selected_song

    # Scrape the lyrics for the selected song
    lyrics = lyrics_scraper.scrape_lyrics(artist, song_name)

    # Update the lyrics text area with the scraped lyrics
    lyrics_text.delete(1.0, END)
    lyrics_text.insert(END, lyrics)


# Add a button to initiate lyrics scraping
scrape_button = Button(lyrics_frame, text="Scrape Lyrics", command=fetch_lyrics)
scrape_button.pack()


# Run the main application loop
root.mainloop()
