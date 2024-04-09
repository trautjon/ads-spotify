import pandas as pd

def create_dataframe_from_playlist(spotify_playlist_songs):

    # Extrahiere die erforderlichen Daten
    track_ids = []
    artist_names = []
    track_names = []
    popularity = []
    explicit = []

    for item in spotify_playlist_songs['items']:
        track_ids.append(item['track']['id'])
        artist_names.append(item['track']['artists'][0]['name'])
        track_names.append(item['track']['name'])
        popularity.append(item['track']['popularity'])
        explicit.append(item['track']['explicit'])

    # Erstelle ein Pandas DataFrame
    df = pd.DataFrame({
        'Track_ID': track_ids,
        'Artist_Name': artist_names,
        'Track_Name': track_names,
        'Popularity': popularity,
        'Explicit': explicit
    })

    return df

def create_dataframe_from_audiofeautures(track_audiofeatures_dict):

    # Audio-Merkmale in ein DataFrame umwandeln
    audiofeatures_df = pd.DataFrame(track_audiofeatures_dict['audio_features'])

    return audiofeatures_df

def merge_basic_song_table_with_song_feautures(basic_song_table, song_feautures_table):

    # Zusammenführen der DataFrames anhand der Track-ID
    merged_df = pd.merge(basic_song_table, song_feautures_table[['id', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']], left_on='Track_ID', right_on='id', suffixes=('', '_audio'))

    # Die 'id' Spalte wird nicht mehr benötigt
    merged_df.drop('id', axis=1, inplace=True)

    return merged_df


