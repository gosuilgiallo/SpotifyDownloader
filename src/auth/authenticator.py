import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAuthenticator:
    """
    Class responsible for authenticating with the Spotify API.
    """
    def __init__(self, credentials_file='credentials.json'):
        self.credentials_file = credentials_file
        self.client_id = None
        self.client_secret = None
        
    def load_credentials(self):
        """Loads credentials from the JSON file."""
        try:
            with open(self.credentials_file, 'r') as f:
                data = json.load(f)
                spotify_credentials = data.get("spotify_credentials", {})[0]
                self.client_id = spotify_credentials.get("client_id")
                self.client_secret = spotify_credentials.get("client_secret")
                
            if not self.client_id or not self.client_secret:
                raise ValueError("Missing Spotify credentials in the file")
                
            return True
        except Exception as e:
            print(f"Error loading credentials: {e}")
            return False
    
    def authenticate(self):
        """Authenticates with Spotify and returns an authenticated client."""
        if not self.client_id or not self.client_secret:
            if not self.load_credentials():
                raise ValueError("Unable to authenticate without valid credentials")
        
        client_credentials_manager = SpotifyClientCredentials(self.client_id, self.client_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)