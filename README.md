# Spotify Playlist Downloader

This Python project allows you to download Spotify playlists directly to your computer in MP3 format, while preserving the original track metadata.

## Key Features

*   **Playlist Download:** Download entire Spotify playlists by providing the link.
*   **Full Metadata:** Retains track metadata (artist, title, album, year, etc.) using the Spotify API.
*   **Custom File Names:** MP3 files are saved in the format "Artist - Song Title.mp3".
*   **Graphical Interface:** Simple and intuitive user interface with a progress bar.
*   **Error Handling:** Includes error handling for network issues, file not found, etc.

## Requirements

*   Python 3.x
*   Libraries: `spotipy`, `yt-dlp`, `eyed3`
*   Spotify API Credentials: Get your `client_id` and `client_secret` by registering your application on [Spotify for Developers](https://developer.spotify.com/dashboard/applications).

## Installation

1.  **Clone the repository:** `git clone https://github.com/gosuilgiallo/spotify-playlist-downloader.git`
2.  **Install dependencies:** `pip install -r requirements.txt`
3.  **Enter Spotify credentials:**
    *   Open the file `downloader.py`.
    *   Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with your credentials.

## Usage

1.  **Run the program:** `python main.py`
2.  **Enter the Spotify playlist link** in the provided text box.
3.  **Click the "Download" button.**
4.  **Choose the destination folder** to save the MP3 files.
5.  **Wait for the download to complete.** The progress bar will show you the progress.

## Customization (Optional)

*   **Download Format:** Modify `ydl_opts` in `downloader.py` to choose formats other than MP3 (e.g., FLAC).
*   **Additional Metadata:** Add logic to extract and save other metadata like BPM or music genre.

## Disclaimer

*   Using this script to download copyrighted music may violate Spotify's terms of service. Use it responsibly.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.
