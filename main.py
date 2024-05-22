import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import os

CLIENT_ID = '1df740f1d4fe4d40873815da97b35879'
CLIENT_SECRET = '5e9e029a9d2945ffa3810712f8eadb4f'

def playlist_model(playlist_id, model, num_songs=10, max_gen=3, same_art=5):
    log = []
    Fresult = []
    try:
        log.append('Start logging')
        uri = playlist_id
        try:
            log.append('spotify local method')
            stream = open("Spotify/Spotify.yaml")
            spotify_details = yaml.safe_load(stream)
            auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        except:
            log.append('spotify .streamlit method')
            try:
                auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
            except:
                log.append('spotify hug method')
                auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        if model == 'Spotify Model':
            def get_IDs(user, playlist_id):
                try:
                    log.append('start playlist extraction')
                    track_ids = []
                    playlist = sp.user_playlist(user, playlist_id)
                    for item in playlist['tracks']['items']:
                        track = item['track']
                        track_ids.append(track['id'])
                    return track_ids
                except Exception as e:
                    log.append('Failed to load the playlist')
                    log.append(e)

            track_ids = get_IDs('Ruby', uri)
            track_ids_uni = list(set(track_ids))
            log.append('Starting Spotify Model')
            Spotifyresult = pd.DataFrame()
            for i in range(len(track_ids_uni) - 5):
                if len(Spotifyresult) >= num_songs:
                    break
                try:
                    ff = sp.recommendations(seed_tracks=list(track_ids_uni[i:i + 5]), limit=5)
                except Exception as e:
                    log.append(e)
                    continue
                for z in range(5):
                    result = pd.DataFrame([z + (5 * i) + 1])
                    result['uri'] = ff['tracks'][z]['id']
                    result['name'] = ff['tracks'][z]['name']
                    result['artist'] = ff['tracks'][z]['artists'][0]['name']
                    Spotifyresult = pd.concat([Spotifyresult, result], axis=0)
                    Spotifyresult.drop_duplicates(subset=['uri'], inplace=True, keep='first')
                Fresult = Spotifyresult[:num_songs]

            log.append('Model run successfully')
            return Fresult, log

        lendf = len(pd.read_csv('Data/streamlit.csv', usecols=['track_uri']))
        dtypes = {'track_uri': 'object', 'artist_uri': 'object', 'album_uri': 'object', 'danceability': 'float16',
                  'energy': 'float16', 'key': 'float16',
                  'loudness': 'float16', 'mode': 'float16', 'speechiness': 'float16', 'acousticness': 'float16',
                  'instrumentalness': 'float16',
                  'liveness': 'float16', 'valence': 'float16', 'tempo': 'float16', 'duration_ms': 'float32',
                  'time_signature': 'float16',
                  'Track_release_date': 'int8', 'Track_pop': 'int8', 'Artist_pop': 'int8', 'Artist_genres': 'object'}
        col_name = ['track_uri', 'artist_uri', 'album_uri', 'danceability', 'energy', 'key',
                    'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                    'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                    'Track_release_date', 'Track_pop', 'Artist_pop', 'Artist_genres']

        try:
            def get_IDs(user, playlist_id):
                log.append('start playlist extraction')
                track_ids = []
                artist_id = []
                playlist = sp.user_playlist(user, playlist_id)
                for item in playlist['tracks']['items']:
                    track = item['track']
                    track_ids.append(track['id'])
                    artist = item['track']['artists']
                    artist_id.append(artist[0]['id'])
                return track_ids, artist_id
        except Exception as e:
            log.append('Failed to load the playlist')
            log.append(e)

        track_ids, artist_id = get_IDs('Ruby', uri)
        log.append("Number of Track : {}".format(len(track_ids)))

        artist_id_uni = list(set(artist_id))
        track_ids_uni = list(set(track_ids))
        log.append("Number of unique Artists : {}".format(len(artist_id_uni)))
        log.append("Number of unique Tracks : {}".format(len(track_ids_uni)))

        def extract(track_ids_uni, artist_id_uni):
            err = []
            err.append('Start audio features extraction')
            audio_features = pd.DataFrame()
            for i in range(0, len(track_ids_uni), 25):
                try:
                    track_feature = sp.audio_features(track_ids_uni[i:i + 25])
                    track_df = pd.DataFrame(track_feature)
                    audio_features = pd.concat([audio_features, track_df], axis=1)
                except Exception as e:
                    err.append(e)
            audio_features.columns = col_name
            err.append('Extraction completed')
            return audio_features, err

        log.append('Audio features extraction')
        audio_features, err = extract(track_ids_uni, artist_id_uni)
        if len(err) > 1:
            log.append('Errors occured : {}'.format(len(err)))
        return audio_features, log

    except Exception as e:
        log.append('Exception: {}'.format(e))
        return Fresult, log

def playlist_analysis(playlist_id):
    log = []
    try:
        log.append('Start playlist analysis')
        uri = playlist_id
        try:
            log.append('spotify local method')
            stream = open("Spotify/Spotify.yaml")
            spotify_details = yaml.safe_load(stream)
            auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        except:
            log.append('spotify .streamlit method')
            try:
                auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
            except:
                log.append('spotify hug method')
                auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        
        def get_playlist_tracks(user, playlist_id):
            log.append('Extracting playlist tracks')
            tracks = []
            playlist = sp.user_playlist(user, playlist_id)
            for item in playlist['tracks']['items']:
                track = item['track']
                track_info = {
                    'name': track['name'],
                    'artist': track['artists'][0]['name'],
                    'uri': track['id']
                }
                tracks.append(track_info)
            return tracks
        
        tracks = get_playlist_tracks('Ruby', uri)
        log.append('Playlist analysis completed')
        return tracks, log
    
    except Exception as e:
        log.append('Exception: {}'.format(e))
        return [], log
