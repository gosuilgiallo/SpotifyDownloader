class SpotifyContentIdentifier:
    """
    Classe responsabile per l'identificazione e il recupero dei contenuti Spotify.
    """
    def __init__(self, spotify_client):
        self.sp = spotify_client
        
    def identify_content(self, spotify_link):
        """
        Identifica il tipo di contenuto Spotify e restituisce le informazioni pertinenti.
        """
        content_id = spotify_link.split("/")[-1].split("?")[0]
        
        if "playlist" in spotify_link:
            return self._process_playlist(content_id)
        elif "album" in spotify_link:
            return self._process_album(content_id)
        elif "track" in spotify_link:
            return self._process_track(content_id)
        else:
            raise ValueError("Unsupported Spotify link provided")
    
    def _process_playlist(self, content_id):
        content = self.sp.playlist(content_id)
        return {
            'content': content,
            'tracks': content['tracks']['items'],
            'content_name': content['name'],
            'is_playlist': True
        }
    
    def _process_album(self, content_id):
        content = self.sp.album(content_id)
        return {
            'content': content,
            'tracks': content['tracks']['items'],
            'content_name': content['name'],
            'is_playlist': False
        }
    
    def _process_track(self, content_id):
        content = self.sp.track(content_id)
        return {
            'content': content,
            'tracks': [{'track': content}],
            'content_name': content['name'],
            'is_playlist': False
        }