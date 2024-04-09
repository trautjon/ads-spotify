
import api_handler as api
import dataframe_handler as dataframe

token = api.get_token()

playlist_user_input = input("Bitte gebe die Playlist ein, welche du suchen möchtest (Format Top 50 - LAND/Global): ")

playlist_id = api.search_for_playlist(token, playlist_user_input)

song_data = api.get_songs_of_playlist(token, playlist_id)

basic_song_table = dataframe.create_dataframe_from_playlist(song_data)

song_feautures = api.get_song_features(token, basic_song_table)

basic_audiofeautures_table = dataframe.create_dataframe_from_audiofeautures(song_feautures)

charts_df = dataframe.merge_basic_song_table_with_song_feautures(basic_song_table, basic_audiofeautures_table)

#Zum Debuggen

#print(charts_df)
charts_df.to_excel(playlist_user_input + ".xlsx")