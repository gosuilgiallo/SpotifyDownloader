import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import eyed3
import os
import tkinter as tk
from tkinter import ttk
import time

def download_spotify_playlist(playlist_link, download_path):
    """
    Downloads a Spotify playlist and its tracks to a folder named after the playlist.
    """

    # Spotify Authentication
    client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Get playlist information
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    playlist = sp.playlist(playlist_id)

    # Create playlist folder
    playlist_folder = os.path.join(download_path, playlist['name'])
    os.makedirs(playlist_folder, exist_ok=True)

    # Create download window
    download_window = tk.Toplevel()
    download_window.title(f"Downloading {playlist['name']}")
    download_window.configure(bg="white")

    # Download status label
    status_label = ttk.Label(download_window, text="Downloading files...", font=("Arial", 12), background="white")
    status_label.pack(pady=10)

    # Progress bar
    progress_bar = ttk.Progressbar(download_window, orient="horizontal", length=300, mode="determinate", style="Horizontal.TProgressbar")
    progress_bar.pack(pady=10)

    # Download tracks
    failed_tracks = []
    total_tracks = len(playlist['tracks']['items'])
    progress_bar['maximum'] = total_tracks

    start_time = time.time()  # Start time of the download

    for i, item in enumerate(playlist['tracks']['items']):
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{playlist_folder}/{artist_name} - {track_name}.%(ext)s',  # Save in playlist folder
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"ytsearch1:{track_name} {artist_name}"])

            # Update metadata (artist and title only)
            mp3_file = f"{playlist_folder}/{artist_name} - {track_name}.mp3"
            if os.path.exists(mp3_file):
                audiofile = eyed3.load(mp3_file)
                audiofile.tag.artist = artist_name
                audiofile.tag.title = track_name
                audiofile.tag.save()
        except Exception as e:
            print(f"Error downloading {artist_name} - {track_name}: {e}")
            failed_tracks.append(f"{artist_name} - {track_name}")

        # Update progress bar and label
        progress_bar['value'] = i + 1
        progress_bar.update()

        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / (i + 1)) * (total_tracks - i - 1)
        status_label.config(text=f"Downloaded: {i + 1}/{total_tracks} (Remaining: {int(remaining_time)}s)")
        download_window.update()

    # Show download results
    if failed_tracks:
        status_label.config(text=f"Download complete with {len(failed_tracks)} failures. See below:")
        for track in failed_tracks:
            ttk.Label(download_window, text=f"- {track}", background="white").pack()
    else:
        status_label.config(text="Download complete!")
