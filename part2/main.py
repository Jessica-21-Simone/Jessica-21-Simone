from modules.instruments import Guitar, Piano, Drum, Instrument
from modules.song import Song
from modules.playlist import Playlist
from modules.utils import print_section_separator

import json



# 2.1.3. Fonction à compléter après avoir compléter le code de modules/instruments.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testInstruments():
  
  print_section_separator("Tests partie 2.1")
  
  # TODO: Instancier un objet de la classe Instrument.
  
  try:
        instrument = Instrument("fabricant-i")  # Devrait lever une exception
  except TypeError:
        print("Impossible d'instancier un Instrument.")
  
  

  # TODO: Instancier une Guitar du "fabricant-g", l'afficher, et appeler sa méthode play().
  
  guitar = Guitar("fabricant-g")
  print(guitar)
  guitar.play()
  
  

  # TODO: Instancier un Piano du "fabricant-p", l'afficher, et appeler sa méthode play().
  
  
  piano = Piano("fabricant-p")
  print(piano)
  piano.play()
  
  

  # TODO: Instancier un Drum du "fabricant-b", l'afficher, et appeler sa méthode play().
  
  drum = Drum("fabricant-b")
  print(drum)
  drum.play()

# 2.2.6. Fonction à compléter après avoir compléter le code de modules/song.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testSong():
  
  print_section_separator("Tests partie 2.2")

  # TODO: Instancier une Song appelée "Title", de l'artiste "Artist",
  #       sortie en 2024 et qui se joue avec une batterie du fabriquant "brand".
  #       Afficher l'instance créée.
try:
       drum_instrument = Drum("brand")
       Music = Song("Title", "Artist", 2024, drum_instrument)
       print(Music)
except Exception as e:
        print(f"Erreur inattendue: {e}")

  # TODO: Instancier une Song à partir d'un dictionnaire/objet vide (i.e. {}).
  #       Afficher l'instance créée.
  
  
try:
      song_from_empty_dict = Song.from_obj({})
      print(song_from_empty_dict)
except ValueError as e:
        # Afficher l'exception capturée
        print(f"ValueError, message: {e}")
        

  # TODO: Instancier une Song à partir de la 1ère chanson du fichier "data/songs.json"
  #       Afficher l'instance créée.
try:
        first_data = json.load(open("part2\data\songs.json"))[0]  # Charger le premier élément du fichier JSON
        song_from_json = Song.from_obj(first_data)
        # Afficher l'instance créée
        print(song_from_json)
except Exception as e:
        print(f"Erreur lors de l'instanciation de la chanson depuis JSON: {e}")



# 2.3.6. Fonction à compléter après avoir compléter le code de modules/playlist.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testPlaylist():
 
  print_section_separator("Tests partie 2.3")

  # TODO: Instancier une Playlist nommée "Playlist-csv" depuis le fichier CSV data/songs.csv.

  try:
        playlist_csv = Playlist.from_csv("Playlist-csv", "part2\data\songs.csv")
  except Exception as e:
        print(f"Erreur lors de l'instanciation de la Playlist depuis CSV: {e}")

  # TODO: Instancier une Playlist nommée "Playlist-json" depuis le fichier JSON data/songs.json.
  
  try:
    playlist_json = Playlist.from_json("Playlist-json", "part2\data\songs.json")
  except Exception as e:
        print(f"Erreur lors de l'instanciation de la Playlist depuis JSON: {e}")
  

  # TODO:Ajouter un dictionnaire/objet vide (i.e. {}) à la playlist "Playlist-json".
  try:
      playlist_json + {}
  except TypeError as e:
        print(f"TypeError, message: {e}")
  
  # TODO: Ajouter les chansons de la playlist "Playlist-json" à la playlist "Playlist-csv".

  for song in playlist_json:
        playlist_csv += song
   
  
  # TODO: Retirer la chanson intitulée "We Will Rock You" de la playlist "Playlist-csv".
  playlist_csv -= "We Will Rock You"
  

  # TODO: Jouer toutes les chansons de la playlist "Playlist-json" en mode normal.
  
  playlist_json.play_all(rdm_mode=False)

  #TODO: Jouer toutes les chansons de la playlist "Playlist-csv" en mode aléatoire.
  playlist_csv.play_all(rdm_mode=True)


if __name__ == "__main__":
  testInstruments()
  testSong()
  testPlaylist()
