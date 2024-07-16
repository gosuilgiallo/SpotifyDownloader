import tkinter as tk
from tkinter import ttk, filedialog
import downloader
import threading

def download_playlist():
    playlist_link = link_entry.get()
    download_path = filedialog.askdirectory(initialdir=".", title="Select Download Folder")

    # Clear the input box and reset the hint
    link_entry.delete(0, tk.END)
    link_entry.insert(0, "Insert Spotify playlist link")

    # If a download path was selected, start the download in a separate thread
    if download_path:
        threading.Thread(target=downloader.download_spotify_playlist, args=(playlist_link, download_path)).start()

# Create main window
window = tk.Tk()
window.title("Download Spotify Playlist")
window.configure(bg="white")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#4285F4", foreground="white", borderwidth=0, padding=10)
style.configure("TEntry", padding=8)
style.configure("Horizontal.TProgressbar", background="green")  # Green progress bar

# Label and Entry
title_label = ttk.Label(window, text="Download Spotify Playlist", font=("Arial", 16), background="white")
title_label.pack(pady=20)

link_entry = ttk.Entry(window, width=50)
link_entry.insert(0, "Insert Spotify playlist link")
link_entry.pack()

# Download Button
download_button = ttk.Button(window, text="Download", command=download_playlist)
download_button.pack(pady=20)

window.mainloop()
