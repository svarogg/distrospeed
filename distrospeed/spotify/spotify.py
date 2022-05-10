import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class Spotify:
    def __init__(self, creds):
        spotify_creds = creds["spotify"]
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_creds["client_id"],
                                                                            client_secret=spotify_creds[
                                                                                "client_secret"]))

    def search(self, query):
        return self.client.search(q='query')
