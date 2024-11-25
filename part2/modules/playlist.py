from modules.song import Song
from typing import Iterator
import csv, json, random
from random import shuffle

class Playlist:
    def __init__(self, name: str, songs: list[Song]):
        if not name.startswith("Playlist-"):
            raise ValueError("Le nom de la playlist doit commencer par 'Playlist-'.")
        self.__name = name
        self.__songs = {song.title: song for song in songs}

    
    @classmethod
    def from_csv(cls, name: str, csv_path: str):
        songs = []
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                song = Song.from_obj(row)
                songs.append(song)
        return cls(name, songs)

   
    @classmethod
    def from_json(cls, name: str, json_path: str):
        songs = []
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for obj in data:
                song = Song.from_obj(obj)
                songs.append(song)
        return cls(name, songs)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if not name.startswith("Playlist-"):
            raise ValueError("Le nom de la playlist doit commencer par 'Playlist-'.")
        self.__name = name

    @property
    def songs(self) -> dict[str, Song]:
        return self.__songs

    @songs.setter
    def songs(self, songs: list[Song]):
        self.__songs = {song.title: song for song in songs}

 
    def __iter__(self) -> Iterator[Song]:
        return iter(self.__songs.values())

   
    def __add__(self, song: Song):
        if isinstance(song, Song):
            self.__songs[song.title] = song
            return self
        else:
            raise TypeError(f"Impossible d'ajouter une chanson de type {type(song)}.")

    
    def __sub__(self, song_title: str):
        if song_title in self.__songs:
            del self.__songs[song_title]
        return self

    def play_all(self, rdm_mode: bool = False):
        mode = "aléatoire" if rdm_mode else "standard"
        print(f"Lecture de {self.__name} ({len(self.__songs)} chansons en mode {mode})")

        # Ordre de lecture
        song_list = list(self.__songs.values())
        if rdm_mode:
            random.shuffle(song_list)

        for song in song_list:
            song.play()