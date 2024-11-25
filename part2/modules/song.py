import modules.instruments # used in from_obj() classmethod
from modules.instruments import Instrument
from datetime import datetime


class Song():
  max_len_str_attr = 25

  def __init__(self, title: str, artist: str, release_year: int, instrument: Instrument):
        # Vérification des contraintes et initialisation des attributs
        if not (0 <= len(title) <= self.max_len_str_attr):
            raise ValueError(f"Le titre doit avoir une longueur entre 0 et {self.max_len_str_attr}.")
          
        if not (0 <= len(artist) <= self.max_len_str_attr):
            raise ValueError(f"L'artiste doit avoir une longueur entre 0 et {self.max_len_str_attr}.")
          
        current_year = datetime.now().year
        if not (0 <=int( release_year) <= int(current_year)):
            raise ValueError(f"L'année de sortie doit être comprise entre 0 et l'année actuelle ({current_year}).")
        if not isinstance(instrument, Instrument):
            raise ValueError("L'instrument doit être une instance de la classe Instrument.")
          
          
        self.__title = title
        self.__artist = artist
        self.__release_year = release_year
        self.__instrument = instrument

  
  @classmethod
  def from_obj(cls, obj: dict):
        
        # Vérification des champs dans le dictionnaire
        required_fields = ["title", "artist", "release_year", "instrument", "instrument_brand"]
        for field in required_fields:
            if field not in obj:
                raise ValueError(f"Impossible d'instancier une chanson depuis l'objet '{obj}'.")
          # Création de l'instrument
        instrument_cls = getattr(modules.instruments, obj["instrument"])
        instrument_instance = instrument_cls(obj["instrument_brand"])
          
        
        # Création de l'instance de Song
        return cls(
            title=obj["title"],
            artist=obj["artist"],
            release_year=int(obj["release_year"]),
            instrument=instrument_instance
        )

  
       # Getters
  @property
  def title(self) -> str:
        return self.__title
    
  @property
  def artist(self) -> str:
        return self.__artist
    
  @property
  def release_year(self) -> int:
        return self.__release_year
    
  @property
  def instrument(self) -> Instrument:
        return self.__instrument
    
    # Setters
  @title.setter
  def title(self, title: str):
        if len(title) > Song.max_len_str_attr:
            raise ValueError(f"Le titre ne peut pas dépasser {Song.max_len_str_attr} caractères.")
        self.__title = title
        
  @artist.setter
  def artist(self, artist: str):
        if len(artist) > Song.max_len_str_attr:
            raise ValueError(f"L'artiste ne peut pas dépasser {Song.max_len_str_attr} caractères.")
        self.__artist = artist
    
  @release_year.setter
  def release_year(self, release_year: int):
        current_year = datetime.now().year
        if release_year < 0 or release_year > current_year:
            raise ValueError(f"L'année de sortie doit être comprise entre 0 et {current_year}.")
        self.__release_year = release_year
    
  @instrument.setter
  def instrument(self, instrument: Instrument):
        if not isinstance(instrument, Instrument):
            raise TypeError("L'instrument doit être une instance de la classe Instrument ou de ses sous-classes.")
        self.__instrument = instrument

    # Méthode __repr__ pour une meilleure représentation de l'objet Song

  def __str__(self) -> str:
      
        return f"Titre: {self.__title}\n" \
               f" Artiste: {self.__artist}\n" \
               f" Annee de sortie: {self.__release_year}\n" \
               f" Instrument: {self.__instrument}"
               
               
               
  def play(self):
       
        instrument_name = self.__instrument.__class__.__name__.lower()  # Nom de l'instrument (Guitar, Piano, Drum)
        brand = self.__instrument._brand  # Récupère le fabricant de l'instrument
        
        # Affiche le message en utilisant le titre de la chanson, le nom de l'instrument et le fabricant
        print(f"Joue {self.__title}    solo avec *** {instrument_name} *** du fabricant {brand}")