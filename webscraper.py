from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
def get_playlist_names():
    # Initialisieren vom Browser
    driver = webdriver.Firefox()
    try:
        # Link der gewünschten Seite
        driver.get("https://open.spotify.com/genre/section0JQ5DAzQHECxDlYNI6xD1i")
        # Wartezeit, um die Seite zu laden
        time.sleep(4)
        # Alle Elemente finden basierend auf ID
        playlists = driver.find_elements(By.XPATH, '//p[contains(@id,"card-title-spotify:playlist:")]')
        # Erstellen einer Liste mit den Suchergebnissen
        playlist_titles = [playlist.text for playlist in playlists if 'Top 50' in playlist.text]
        # Gibt die Liste der Titel zurück
        return playlist_titles
    finally:
        # Schließen des Browsers
        driver.quit()
 
# Verwendung der Funktion, um die Playlist-Titel zu erhalten und auszugeben
#playlist_names = get_playlist_names()
#print("Gefundene Playlists:")
#for name in playlist_names:
#    print(name)