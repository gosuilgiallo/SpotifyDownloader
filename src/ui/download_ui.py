import tkinter as tk
from tkinter import ttk
import time

class DownloadUI:
    """
    Classe responsabile della gestione dell'interfaccia utente per il download.
    """
    def __init__(self, content_name):
        self.download_window = tk.Toplevel()
        self.download_window.title(f"Downloading {content_name}")
        self.download_window.configure(bg="white")
        
        # Download status label
        self.status_label = ttk.Label(
            self.download_window, 
            text="Preparing download...", 
            font=("Arial", 12), 
            background="white"
        )
        self.status_label.pack(pady=10)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            self.download_window, 
            orient="horizontal", 
            length=300, 
            mode="determinate", 
            style="Horizontal.TProgressbar"
        )
        self.progress_bar.pack(pady=10)
        
        # Start timing
        self.start_time = time.time()
        
    def set_total_tracks(self, total):
        """Imposta il numero totale di tracce per la progress bar."""
        self.progress_bar['maximum'] = total
        self.status_label.config(text="Downloading files...")
        self.download_window.update()
        
    def update_progress(self, current, total):
        """Aggiorna la progress bar e il testo di stato."""
        self.progress_bar['value'] = current
        
        elapsed_time = time.time() - self.start_time
        if current > 0:  # Evita divisione per zero
            remaining_time = (elapsed_time / current) * (total - current)
            self.status_label.config(text=f"Downloaded: {current}/{total} (Remaining: {int(remaining_time)}s)")
        
        self.download_window.update()
        
    def show_completion_status(self, failed_tracks):
        """Mostra lo stato di completamento del download."""
        if failed_tracks:
            self.status_label.config(text=f"Download complete with {len(failed_tracks)} failures. See below:")
            for track in failed_tracks:
                ttk.Label(self.download_window, text=f"- {track}", background="white").pack()
        else:
            self.status_label.config(text="Download complete!")
        
        self.download_window.update()