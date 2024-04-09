
import base64
import json
from requests import post, get


#client id und client_secret setzen

with open("api-keys.json", "r") as key_datei:
    key_datei_daten = json.load(key_datei)


client_id = key_datei_daten["client_id"]
client_secret = key_datei_daten["client_secret"]




def get_token():

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    
    headers = {
        "Authorization": "Basic " + auth_base64, 
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query

    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)["playlists"]["items"]

    if len(json_result) == 0:
        print("Keine Playlist gefunden - Bitte an das Format 'Top 50 - Land' halten (oder 'Global' anstelle von 'Land').")
        return None
    else:
        
        pid = json_result[0]["id"]
        pname = json_result[0]["name"]

        print("Playlist "+pname+" mit ID: "+pid+" gefunden!")
        
        return pid
    
def get_songs_of_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=2"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content) #json.loads() kreiert ein Python dictonary - Kein Json
    
    return json_result

def get_song_features(token, basic_song_table):

    #IDs aus Dataframe holen und IDs mit Komma aneinander hängen

    track_ids = basic_song_table['Track_ID'].tolist()

    # Konvertiere die IDs in einen String mit dem gewünschten Format
    
    track_ids_string = ','.join(track_ids)

    print("ID Liste wurde erstellt: " + track_ids_string)

    #IDs an API senden

    url = f"https://api.spotify.com/v1/audio-features?ids={track_ids_string}"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)

    return json_result #Python Dictionary 

# Zum Debuggen

#token = get_token()
#result = search_for_playlist(token, "Top 50 - Switzerland") 

#playlist_id = pid

#songs = get_songs_of_playlist(token,playlist_id)

#panda_table = create_dataframe_from_playlist(songs)
#print(panda_table)