from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#TODO: Webscraper scolled den Inhalt nicht, was dazu führt, dass nur 20 Listen geladen werden; Momentaner Workaround - Im Browserfenster manuell bis zum Ende scrollen.  

def get_playlist_names():
    # Initialisieren vom Browser
    driver = webdriver.Firefox()
    try:
        # Link der gewünschten Seite
        driver.get("https://open.spotify.com/genre/section0JQ5DAzQHECxDlYNI6xD1i")
        
        # Warten Sie, bis die Seite geladen ist, und scrollen Sie dann nach unten.
        time.sleep(2)
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(50):  # Die Anzahl der Iterationen sollte ausreichend sein, um das Ende der Seite zu erreichen.
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # Warte einen Moment, damit Inhalte nachgeladen werden können.
 
        # Nach dem Scrollen alle Playlists erfassen
        playlists_elements = driver.find_elements(By.XPATH, '//p[contains(@id,"card-title-spotify:playlist:")]')
 
        playlist_titles = [element.text for element in playlists_elements if 'Top 50' in element.text]
        
        
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