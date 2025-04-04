import tkinter as tk
from tkinter import ttk, filedialog
import threading
import downloader.downloader as downloader

class AppUI:
    """
    Classe responsabile della gestione dell'interfaccia utente principale.
    """
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Download Spotify content")
        self.window.configure(bg="white")
        
        # Styling
        self._setup_styles()
        
        # UI Components
        self._create_widgets()
    
    def _setup_styles(self):
        """Configura gli stili dell'interfaccia."""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#4285F4", foreground="white", borderwidth=0, padding=10)
        style.configure("TEntry", padding=8)
        style.configure("Horizontal.TProgressbar", background="green")  # Green progress bar
    
    def _create_widgets(self):
        """Crea e posiziona i widget dell'interfaccia."""
        # Label and Entry
        title_label = ttk.Label(self.window, text="Download Spotify content", font=("Arial", 16), background="white")
        title_label.pack(pady=20)
        
        self.link_entry = ttk.Entry(self.window, width=50)
        self.link_entry.insert(0, "Insert Spotify content link")
        self.link_entry.pack()
        
        # Download Button
        download_button = ttk.Button(self.window, text="Download", command=self._download_content)
        download_button.pack(pady=20)
    
    def _download_content(self):
        """Gestisce l'evento di click sul pulsante di download."""
        content_link = self.link_entry.get()
        download_path = filedialog.askdirectory(initialdir=".", title="Select Download Folder")
        
        # Clear the input box and reset the hint
        self.link_entry.delete(0, tk.END)
        self.link_entry.insert(0, "Insert Spotify link")
        
        # If a download path was selected, start the download in a separate thread
        if download_path:
            threading.Thread(target=downloader.download_spotify_content, args=(content_link, download_path)).start()
    
    def run(self):
        """Avvia il loop principale dell'interfaccia."""
        self.window.mainloop()