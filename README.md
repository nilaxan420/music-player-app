Music Player Application

The Music Player Application is a graphical user interface (GUI) application built using Python and Tkinter. It allows users to play songs from a Spotify playlist, display album images, and scrape lyrics for the selected song.

Features
Fetches top songs from a Spotify playlist using the Spotify API.
Displays album images for the selected song using the Spotify API.
Plays songs using the Pygame library.
Scrapes lyrics for the selected song from a lyrics website.
Provides control buttons to play, stop, and navigate through songs.
Prerequisites
Python 3.7 or higher
Tkinter library
Pygame library
PIL library
Requests library
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/music-player-app.git
Install the required libraries:

Copy code
pip install -r requirements.txt
Run the application:

Copy code
python music_player.py
Usage
Launch the Music Player application.
The top songs from the Spotify playlist will be fetched and displayed in the listbox.
Select a song from the listbox to display its album image in the left frame.
Use the control buttons (Prev, Stop, Play, Next) to navigate and play songs.
Click the "Scrape Lyrics" button to fetch and display the lyrics for the selected song.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Implement your feature or bug fix.
Commit and push your changes.
Submit a pull request.
