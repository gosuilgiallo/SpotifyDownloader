import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import eyed3
import os
import tkinter as tk
from tkinter import ttk
import time

def download_spotify_content(spotify_link, download_path):
    """
    Downloads Spotify content (playlist, album, or track) to a folder named after the content.
    """

    # Spotify Authentication
    client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Identify content type
    content_id = spotify_link.split("/")[-1].split("?")[0]
    if "playlist" in spotify_link:
        content = sp.playlist(content_id)
        tracks = content['tracks']['items']
        content_name = content['name']
        is_playlist = True
    elif "album" in spotify_link:
        content = sp.album(content_id)
        tracks = content['tracks']['items']
        content_name = content['name']
        is_playlist = False
    elif "track" in spotify_link:
        content = sp.track(content_id)
        tracks = [{'track': content}]
        content_name = content['name']
        is_playlist = False
    else:
        raise ValueError("Unsupported Spotify link provided")

    # Create content folder
    content_folder = os.path.join(download_path, content_name)
    os.makedirs(content_folder, exist_ok=True)

    # Create download window
    download_window = tk.Toplevel()
    download_window.title(f"Downloading {content_name}")
    download_window.configure(bg="white")

    # Download status label
    status_label = ttk.Label(download_window, text="Downloading files...", font=("Arial", 12), background="white")
    status_label.pack(pady=10)

    # Progress bar
    progress_bar = ttk.Progressbar(download_window, orient="horizontal", length=300, mode="determinate", style="Horizontal.TProgressbar")
    progress_bar.pack(pady=10)

    # Download tracks
    failed_tracks = []
    total_tracks = len(tracks)
    progress_bar['maximum'] = total_tracks

    start_time = time.time()  # Start time of the download

    for i, item in enumerate(tracks):
        if is_playlist:
            track = item['track']
        else:
            track = item  # For albums and single tracks

        track_name = track['name']
        artist_name = track['artists'][0]['name']

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{content_folder}/{artist_name} - {track_name}.%(ext)s',  # Save in content folder
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"ytsearch1:{track_name} {artist_name}"])

            # Update metadata (artist and title only)
            mp3_file = f"{content_folder}/{artist_name} - {track_name}.mp3"
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

# Example usage:
# download_spotify_content('your_spotify_playlist_or_album_or_track_link', '/path/to/download/folder')
