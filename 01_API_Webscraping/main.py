import api_handler as api
import dataframe_handler as dataframe
import webscraper as scraper
import datetime
import os

today = datetime.datetime.now().strftime('%Y-%m-%d')

token = api.get_token()

#playlist_user_input = input("Bitte gebe die Playlist ein, welche du suchen möchtest (Format Top 50 - LAND/Global): ")

playlist_file = "Playlistnames.txt"

#Um effizent zu sein wird nur gescraped, wenn keine Playlistnames.txt vorhanden ist.

if os.path.exists(playlist_file):
    # Lies die Playlist-Namen aus der Datei aus
    with open(playlist_file, "r") as file:
        playlist_user_inputs = file.read().split(",")
else:
    # Rufe scraper.get_playlist_names() auf und speichere die Playlist-Namen in der Datei
    playlist_user_inputs = scraper.get_playlist_names()
    with open(playlist_file, "w") as file:
        file.write(",".join(playlist_user_inputs))


# Testen ob es schon einen Ordner gibt

pfad_zum_ordner = "./" + today

if not os.path.exists(pfad_zum_ordner):
    os.makedirs(pfad_zum_ordner)

# Alle gescrapten Playlist Namen mit Daten bereichern
for playlist in playlist_user_inputs:
 
 #Debugging Info - Welche Playlist gerade durchlaufen wird
 print(playlist)

 playlist_id = api.search_for_playlist(token, playlist)

 song_data = api.get_songs_of_playlist(token, playlist_id)

 basic_song_table = dataframe.create_dataframe_from_playlist(song_data)

 song_feautures = api.get_song_features(token, basic_song_table)

 basic_audiofeautures_table = dataframe.create_dataframe_from_audiofeautures(song_feautures)

 charts_df = dataframe.merge_basic_song_table_with_song_feautures(basic_song_table, basic_audiofeautures_table)

 #Provisorisch im Excelformat speichern

 excel_pfad = os.path.join(pfad_zum_ordner, playlist + " " + today + ".xlsx")
 charts_df.to_excel(excel_pfad)

#Zum Debuggen

#print(charts_df)

#Requirements kann mit "conda list --export > requirements.txt" erstellt werden