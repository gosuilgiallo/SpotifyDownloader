import spotipy
import yt_dlp
import eyed3
import os
import time
from auth.authenticator import SpotifyAuthenticator
from downloader.spotify_content import SpotifyContentIdentifier
from ui.download_ui import DownloadUI

def download_spotify_content(spotify_link, download_path):
    """
    Downloads Spotify content (playlist, album, or track) to a folder named after the content.
    """
    # Authentication
    authenticator = SpotifyAuthenticator()
    sp = authenticator.authenticate()
    
    # Identify content
    content_identifier = SpotifyContentIdentifier(sp)
    content_info = content_identifier.identify_content(spotify_link)
    
    tracks = content_info['tracks']
    content_name = content_info['content_name']
    is_playlist = content_info['is_playlist']
    
    # Create content folder
    content_folder = os.path.join(download_path, content_name)
    os.makedirs(content_folder, exist_ok=True)
    
    # Create download UI
    ui = DownloadUI(content_name)
    
    # Download tracks
    failed_tracks = []
    total_tracks = len(tracks)
    ui.set_total_tracks(total_tracks)
    
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
                'outtmpl': f'{content_folder}/{artist_name} - {track_name}.%(ext)s',
                'noplaylist': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
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
        
        # Update UI progress
        ui.update_progress(i + 1, total_tracks)
    
    # Show download results
    ui.show_completion_status(failed_tracks)