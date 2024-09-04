# Spotify Content Downloader

This Python project allows you to download Spotify content directly to your computer in MP3 format.

## Key Features

*   **Download:** Download entire Spotify playlists, albums or singles by providing the link.
*   **Custom File Names:** Files are saved in the format "Artist - Song Title.mp3".
*   **Graphical Interface:** Simple and intuitive user interface with a progress bar.
*   **Error Handling:** Includes error handling for network issues, file not found, etc.

## Requirements

*   Python 3.x
*   Libraries: `spotipy`, `yt-dlp`, `eyed3`, `ffmpeg`
*   Spotify API Credentials: Get your `client_id` and `client_secret` by registering your application on [Spotify for Developers](https://developer.spotify.com/dashboard/applications).

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gosuilgiallo/spotify-playlist-downloader.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Enter Spotify credentials:**
    *   Open the file `downloader.py`.
    *   Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with your credentials.

## Usage

1.  **Run the program:** ```python main.py```
2.  **Enter the Spotify link** in the provided text box.
3.  **Click the "Download" button.**
4.  **Choose the destination folder** to save the files.
5.  **Wait for the download to complete.** The progress bar will show you the progress.

## Customization (Optional)

*   **Download Format:** Modify `ydl_opts` in `downloader.py` to choose formats other than MP3 (e.g., FLAC).
*   **Additional Metadata:** Add logic to extract and save other metadata like BPM or music genre.

## Disclaimer

*   Using this script to download copyrighted music may violate Spotify's terms of service. Use it responsibly. Some songs may return 403 error and will not be downloaded.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.
