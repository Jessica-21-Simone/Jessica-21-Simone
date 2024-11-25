# Projet 2 : Traitement de données et OOP
⏰ Date de remise le **dimanche 24 novembre à 23h59** directement sur GitHub.

Ce projet se divise en 2 parties distinctes.

#### Partie 1 : Traitement de données

Nous allons **traiter un jeu de données de chansons à l'aide de librairies scientifiques**.
Nous utilisons pour cela un cahier Jupyter, format idéal de travail pour l'exploration de données.

Le répertoire de travail pour cette partie est `part1/`.

Voir instructions détaillées : ^[Partie 1](#partie-1--traitement-de-données-1)

#### Partie 2 : Programmation orientée objet
Nous allons **faire de la programmation orientée objet** pour créer une application qui permet de "jouer" des playlists de chansons à partir d'instruments de musique.

Le répertoire de travail pour cette partie est `part2/`.

Voir instructions détaillées : [Partie 2](#partie-2--programmation-orientée-objet-1)

## Objectifs
À la fin de ce projet, vous aurez pratiquer : 
* l'utilisation de librairies scientifiques *(Chapitre 9)* ;
* la gestion et la résolution de problèmes *(Chapitre 10)* ;
* la programmation orientée objet *(Chapitre 11)*.

## Remarques
- Suivez les conventions de programmation en Python (cf. [guide de codage du cours](https://github.com/INF1007-Gabarits/Guide-codage-python) et normes [PEP 8](https://peps.python.org/pep-0008/)).
- L'anglais est utilisé comme langue de programmation, et le français est utilisé pour les affichages.
- L'ajout de fonctions est autorisé (et suggéré) dans la mesure où celles-ci améliorent la lisibilité du code.

## Structure du projet

```plaintext
<répertoire-principal>/
│   README.md
└─── part1/
│   └─── plots/
│           ...
│        songs-analysis.ipynb
└─── part2/
    └─── data/
    │       songs.csv
    │       songs.json
    └─── modules/
    │       utils.py
    │       instruments.py
    │       song.py
    │       playlist.py
    └─── main.py
```

### Répertoire `part1/`
C'est le répertoire de travail pour compléter la partie 1 du projet.
- `songs.csv` : fichier CSV avec les données de chansons.
- `songs-analysis.ipynb` : fichier Notebook Jupyter où nous allons procéder à l'exploration des chansons.
- `plots/` : contient l'exemple de sorties visuelles attendues depuis le cahier Jupyter.

Pour travailler à partir du cahier Jupyter (dans VS Code) :
- Ouvrez le fichier `songs-analysis.ipynb` et ;
- Assurez-vous d'avoir [configuré le *kernel* approprié](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_create-or-open-a-jupyter-notebook) (correspond à votre exécutable Python).

Vous pouvez ainsi rouler chacune de vos cellules, en cliquant sur l'îcone d'éxécution (triangle côté haut gauche de chaque cellule).
**À chaque fois que vous recommencez à travailler sur votre cahier Jupyter, assurez-vous de ré-exécuter toutes les cellules depuis le début.**

### Répertoire `part2/`
C'est le répertoire de travail pour compléter la partie 2 du projet.
- `data/` : contient un fichier CSV et un fichier JSON avec les données de chansons.
- `modules/` : contient les fichiers où nous allons implémenter les classes de notre application de playlists.
- `main.py` : fichier où nous testerons notre implémentation.

Pour lancer les tests manuelles que vous aurez fait :
- Assurez-vous d'être sous le répertoire `part2/` et ;
- Lancez la commande `python main.py` (`python` ou `python3`) depuis le terminal.
- (ou) Ouvrez le fichier `main.py` dans votre éditeur et cliquez sur l'îcone d'éxécution (flèche en haut à droite de votre onglet).

# Partie 1 : Traitement de données
Notre objectif est de manipuler et de traiter le jeu de données (contenu dans le fichier `songs.csv`) des chansons les plus écoutées sur Spotify en 2024. Nos traitement serviront ensuite à entraîner un modèle simple de régression linéaire pour la prédiction du nombre total d'écoutes d'une chanson sur Spotify.

Le dossier `plots/` contient certaines des sorties attendues du cahier Jupyter. Les *plots* sont numérotées par section.

## Contenu du jeu de données
| Nom de la colonne | Description |
| -- | -- |
| Track Name | Titre de la chanson. |
| Album Name | Nom de l'album auquel la chanson appartient. |
| Artist | Nom de l'artiste ou des artistes de la chanson. |
| Release Date | Date de sortie de la chanson. |
| ISRC | International Standard Recording Code de la chanson. |
| All Time Rank | Classement de la chanson basé sur sa popularité historique. |
| Track Score | Score attribué au titre selon divers facteurs. |
| Spotify Streams | Nombre total d'écoutes sur Spotify. |
| Spotify Playlist Count | Nombre de playlists Spotify contenant la chanson. |
| Spotify Playlist Reach | Portée de la chanson à travers les playlists Spotify. |
| Spotify Popularity | Score de popularité de la chanson sur Spotify. |
| YouTube Views | Nombre total de vues de la vidéo officielle de la chanson sur YouTube. |
| YouTube Likes | Nombre total de likes sur la vidéo officielle de la chanson sur YouTube. |
| TikTok Posts | Nombre de publications TikTok incluant la chanson. |
| TikTok Likes | Nombre total de likes sur les publications TikTok incluant la chanson. |
| TikTok Views | Nombre total de vues sur les publications TikTok incluant la chanson. |
| YouTube Playlist Reach | Portée de la chanson à travers les playlists YouTube. |
| Apple Music Playlist Count | Nombre de playlists Apple Music contenant la chanson. |
| AirPlay Spins | Nombre de fois que la chanson a été diffusée sur les stations de radio. |
| SiriusXM Spins | Nombre de fois que la chanson a été diffusée sur SiriusXM. |
| Deezer Playlist Count | Nombre de playlists Deezer contenant la chanson. |
| Deezer Playlist Reach | Portée de la chanson à travers les playlists Deezer. |
| Amazon Playlist Count | Nombre de playlists Amazon Music contenant la chanson. |
| Pandora Streams | Nombre total d'écoutes sur Pandora. |
| Pandora Track Stations | Nombre de stations Pandora incluant la chanson. |
| Soundcloud Streams | Nombre total d'écoutes sur Soundcloud. |
| Shazam Counts | Nombre total de fois que la chanson a été recherchée sur Shazam. |
| TIDAL Popularity | Score de popularité de la chanson sur TIDAL. |
| Explicit Track | Indique si la chanson contient un contenu explicite. |

## Travail à réaliser
Les instructions détaillées se trouvent directement dans le cahier Jupyter `song-analysis.ipynb`.
- 1.1. Chargement du jeu de données
- 1.2. Exploration des données
- 1.3. Nettoyage des données
- 1.4. Extraction de données
- 1.5. Conversion de données
- 1.6. Visualisation de données
- 1.7. Matrice de corrélation
- 1.8. Entraînement d'un modèle de régression

# Partie 2 : Programmation orientée objet
Notre objectif est de créer un système de lecture de playlists.
On veut être capable de créer des playlists à partir d'une base de données de chansons (enregistrée dans les fichiers `data/songs.csv` et `data/songs.json`) et jouer ces chansons en mode "solo" (à l'aide d'un seul instrument) à partir d'une playlist.

## Vue d'ensemble
Le diagramme ci-bas montre les classes qui vont représenter les objets de notre système ainsi que leurs liens. Par simplicité, seul les attributs des classes et leurs méthodes standards publics y sont représentés.

- Nous implémenterons d'abord la **classe abstraire** `Instrument` qui englobe les caractéristiques communes d'un instrument, et nous créerons les **classes enfants** `Guitar`, `Piano` et `Drum` qui **héritent de `Instrument`**.
- Ensuite, nous implémenterons la classe `Song` qui représente une chanson et ses caractéristiques. Cette classe fait l'**agrégation d'un `Instrument`**, afin de pouvoir jouer la chanson à partir de celui-ci.
- Enfin, nous implémenterons la classe `Playlist` qui fait l'**agrégation d'une liste de `Song` dans un dictionnaire**. Nous pourrons finalement jouer ces chansons à partir d'une `Playlist`.

![Vue d'ensemble](/assets/part2-class-diagram.png)

## Travail à réaliser
### 2.1 Implémenter et tester les classes `Instrument`, `Guitar`, `Piano` et `Drum`
Pour cette section :
- l'implémentation ([2.1.1.](#211-compléter-la-classe-instrument-), [2.1.2.](#212-compléter-les-classes-guitar-piano-drum-)) se fait dans le fichier `modules/instruments.py` ;
- les tests ([2.1.3.](#213-tester-limplémentation)) se font dans la fonction `testInstruments()` du fichier `main.py` ;
- lorsque vous avez terminé les instructions ci-bas, exécutez `main.py` à partir du dossier `part2/` pour voir la sortie de vos tests.

#### 2.1.1. Compléter la classe `Instrument` :
- Rendre la classe abstraite pour qu'elle ne puisse pas être instanciée.
- Définir le constructeur `__init__(self, brand: str)` :
    - La valeur de `brand` est utilisée pour initialiser l'attribut protégé `_brand`.
    - L'attribut `_brand` contient le fabriquant de l'instrument dans une *string*. 
    - Par convention le simple *underscore* définie un attribut protégé ; attribut non accessible à l'extérieur d'un `Instrument` mais accessible depuis les classes qui en héritent.
- Surcharger l'opérateur dont la signature est `__repr__(self) -> str` :
    - Il est implicitement appelée lorsqu'on essaye de représenter notre instance sous forme de *string*, par exemple via un appel à `str()` ou `print()`.
    - Son but est de fournir une représentation officielle de l'instance (ici un `Instrument`) sans ambiguïté.
    - La chaîne de caractère retournée doit avoir le format suivant:
    ```Python
    "Guitar(brand='<fabriquant-de-la-guitare>')"    # Si la classe concrète est Guitar
    "Piano(brand='<fabriquant-du-piano>')"          # Si la classe concrète est Piano
    "Drum(brand='<fabriquant-de-la-batterie>')"     # Si la classe concrète est Drum
    ```
    - À l'intérieur d'une classe, pour obtenir dynamiquement la chaîne de caractère correspondant à son nom ; on peut faire appel à `self.__class__.__name__`.
- Définir la méthode `play(self)` qui doit être abstraite (utilisez un décorateur) et qui n'a aucune implémentation.

#### 2.1.2 Compléter les classes `Guitar`, `Piano`, `Drum` :
- Faire hériter les 3 classes de la classe `Instrument`.
    - Ainsi `Guitar`, `Piano`, `Drum` auront l'attribut `_brand` et les méthodes de `Instrument`.
- Définir le constructeur `__init__(self, brand: str)` pour chacune des classes.
    - Il doit déléguer la création de l'instance au constructeur de la classe parent (il appel le constructeur de `Instrument`).
    - À partir d'une classe enfant, on peut accéder à l'interface d'une classe parent en utilisant `super()`.
- (Re)définir la méthode `play(self)` pour chacune des classes.
    - Cette méthode simule le fait de jouer d'un instrument en affichant un message.
    - Le message affiché doit avoir le format suivant :
    ```Python
    "*** guitare ***  du fabricant <fabriquant-de-la-guitare>"  # Pour la classe Guitar
    "*** piano ***    du fabricant <fabriquant-du-piano>"       # Pour la classe Piano
    "*** batterie *** du fabricant <fabriquant-de-la-batterie>" # Pour la classe Drum
    ```
    - Le nom de l'instrument entouré de 3 étoiles de chaque côté (i.e. `"*** piano ***"`), **doit être aligné à gauche sur `INSTRUMENT_NAME_WIDTH` colonnes**.

#### 2.1.3. Tester l'implémentation
Compléter la fonction `testInstruments()` de `main.py`:
- Instancier un objet de la classe `Instrument`.
    - Cela devrait lancer une exception car la classe `Instrument` est abstraite.
    - Utiliser un mécanisme `try: ... except: ...` pour capturer l'exception.
    - À la capture de l'exception on affiche : `"Impossible d'instancier un Instrument."`.
- Instancier une `Guitar` du fabricant "fabricant-g".
    - Afficher l'instance en la passant directement à la fonction `print()`.
    - Appeler la méthode `play()` sur l'instance.
- Instancier un `Piano` du fabricant "fabricant-p".
    - Afficher l'instance en la passant directement à la fonction `print()`.
    - Appeler la méthode `play()` sur l'instance.
- Instancier un `Drum` du fabricant "fabricant-b".
    - Afficher l'instance en la passant directement à la fonction `print()`.
    - Appeler la méthode `play()` sur l'instance.

Sortie attendue à l'appel de la fonction `testInstruments()` :
```plaintext
=============================== Tests partie 2.1 ===============================
Impossible d'instancier un Instrument.
Guitar(brand='fabricant-g')
*** guitare ***  du fabricant fabricant-g
Piano(brand='fabricant-p')
*** piano ***    du fabricant fabricant-p
Drum(brand='fabricant-b')
*** batterie *** du fabricant fabricant-b
```

### 2.2 Implémenter et tester la classe `Song`
Pour cette section :
- l'implémentation ([2.2.1.](#221-définir-le-constructeur), [2.2.2.](#222-définir-une-méthode-de-classe), [2.2.3.](#223-configurer-laccès-public-aux-attributs-getters-et-setters), [2.2.4.](#224-définir-la-méthode-__str__), [2.2.5.](#225-définir-la-méthode-play)) se fait dans le fichier `modules/song.py` ;
- les tests ([2.2.6.](#226-tester-limplémentation)) se font dans la fonction `testSong()` du fichier `main.py` ;
- lorsque vous avez terminé les instructions ci-bas, exécutez `main.py` à partir du dossier `part2/` pour voir la sortie de vos tests.

#### Description des attributs de `Song` :
| Attribut | Type | Description  | Contrainte |
| --- | --- | --- | --- |
| `max_len_str_attr` | `int` | *Attribut partagé* : la longueur maximale qu'un attribut de type *string* peut avoir dans `Song`. | `max_len_str_attr` a une valeur constante de `25`. |
| `__title` | `str` | *Attribut privé* : le titre de la chanson. | `__title` a une longueur entre [0, `max_len_str_attr`]. |
| `__artist` | `str` | *Attribut privé* : l'artiste de la chanson. | `__artist` a une longueur entre [0, `max_len_str_attr`]. |
| `__release_year` | `int` | *Attribut privé* : l'année de sortie de la chanson. | `__release_year` est compris entre [0, <l'année actuelle>] (utilisez la librairie `datetime` pour obtenir l'année actuelle). |
| `__instrument` | `Instrument` | *Attribut privé* : l'instrument à utiliser pour jouer la chanson en mode "solo". | `__instrument` doit être un `Instrument`. |

#### 2.2.1. Définir le constructeur
- La signature du constructeur est `__init__(self, title: str, artist: str, release_year: int, instrument: Instrument)`.
    - La valeur de `title` est utilisée pour initialiser l'attribut privé `__title`.
    - La valeur de `artist` est utilisée pour initialiser l'attribut privé `__artist`.
    - La valeur de `release_year` est utilisée pour initialiser l'attribut privé `__release_year`.
    - La valeur de instrument est utilisée pour initialiser l'attribut privé `__instrument`.
    - Par convention le double *underscore* définie un attribut privé ; attribut non accessible depuis l'extérieur de la classe `Song`.

**Les contraintes sur les attributs présentées dans [ce tableau](#description-des-attributs-de-song-) doivent être respectées lors de l'initialisation**.

#### 2.2.2. Définir une méthode de classe
Cette méthode de classe nous permettra de construire une instance de `Song` via un objet avec les champs `"title"`, `"artist"`, `"release_year"`, `"instrument"`, `"instrument_brand"`.
- La signature de cette méthode est `from_obj(cls, obj: dict)`, le paramètre `obj` devrait contenir une chanson sous forme de dictionnaire.
- Utiliser un décorateur pour définir la méthode comme méthode de classe.
- Vérifier que l'objet passé en paramètre contient les champs désirés.
    - Si le dictionnaire `obj` ne contient pas tous ces champs, lever une exception `ValueError`, et passer le message suivant :
        ```Python
        "Impossible d'instancier une chanson depuis l'objet '<valeur-de-obj>'."
        ```
- Si le dictionnaire `obj` passe la vérification :
    - Extraire la valeur de chaque attribut de la chanson à partir des champs du dictionnaire `obj`.
        - Utiliser l'instruction ci-bas pour accéder au constructeur de l'`Instrument` désiré (une guitare, un piano ou une batterie) :
            ```Python
            instrument_cls = getattr(modules.instruments, obj["instrument"])
            ```
        - Vous pouvez ensuite y faire appel ainsi `instrument_cls("fabricant-x")` (équivalent à appeler `Piano("fabricant-x")` par exemple).
    - Instancier une `Song` en appelant son constructeur avec `cls(...)` (remplacer les ... par les valeurs des attributs).
    - Retourner l'instance de `Song` que vous venez de construire.

#### 2.2.3. Configurer l'accès public aux attributs privés (*getters* et *setters*)
Pour avoir accès aux attributs privés sans les exposer directement et protéger leur intégrité : nous allons définir des *getters* et des *setters* en utilisant respectivement les décorateurs `@property` et `@<attribute-name>.setter`.

Liste des ***getters*** à implémenter :
- `title(self) -> str` : retourne le titre de la `Song` dans une *string*.
- `artist(self) -> str` : retoure l'artiste de la `Song` dans une *string*.
- `release_year(self) -> int` : retourne l'année de sortie de la `Song` dans un entier.
- `instrument(self) -> Instrument` : retourne l'instrument pour jouer la `Song` dans une instance de `Instrument`.

Liste des ***setters*** à implémenter :
- `title(self, title: str)` : utilise la valeur de `title` pour initialiser le titre.
- `artist(self, artist: str)` : utilise la valeur de `artist` pour initialiser l'artiste.
- `release_year(self, release_year: int)` : utilise la valeur de `release_year` pour initialiser l'année de sortie.
- `instrument(self, instrument: Instrument)` : utilise la valeur de `instrument` pour initialiser l'instrument.

**Les contraintes sur les attributs présentées dans [ce tableau](#description-des-attributs-de-song-) doivent être respectées lors de l'initialisation via ces setters**.

#### 2.2.4. Surcharger l'opérateur `__str__()`
- La signature de cet opérateur est `__str__(self) -> str`, il est implicitement appelée lorsqu'on essaye de représenter notre instance sous forme de *string*, par exemple via un appel à `str()` ou `print()`.
- Son but est de fournir une représentation de l'instance (ici une `Song`) facilement lisible par un humain.
- Un appel à `print()` sur une `Song` doit afficher un message suivant le format ci-bas :
    ```plaintext
    Titre: <titre-de-la-chanson>
     Artiste: <artiste-de-la-chanson>
     Annee de sortie: <annee-sortie-de-la-chanson>
     Instrument: <instrument-de-la-chanson>
    ```
    - Chaque ligne est séparée d'une fin de ligne.
    - Le début des 3 dernières lignes commence par 1 espace.
    - Rappelez-vous que par défaut, la fonction `print()` ajoute une fin de ligne à la chaîne de caractère passée en paramètre.

#### 2.2.5. Définir la méthode `play()`
Cette méthode simule le fait de jouer une chanson à partir de son instrument de "solo" en affichant un message.
- La signature de cette méthode est `play(self)` et elle doit faire appel à la méthode `play()` de son instrument.
- À l'appel de la méthode, le message affiché doit avoir le format suivant :
    ```Python
    "Joue <titre-de-la-chanson>    solo avec *** batterie *** du fabricant <fabriquant-de-l-instrument>" # Par exemple si l'instrument est un Drum
    ```
    - Le titre de la chanson, **doit être aligné à gauche sur `max_len_str_attr` colonnes**.

#### 2.2.6. Tester l'implémentation
Compléter la fonction `testSong()` de `main.py`:
- Instancier une `Song` intitulée "Title", de l'artiste "Artist", sortie en 2024 et qui se joue avec une batterie du fabriquant "brand".
    - Faites appel au constructeur standard.
    - Afficher l'instance en la passant directement à la fonction `print()`.
- Instancier une `Song` à partir d'un dictionnaire/objet vide (i.e. {}).
    - Faites appel à la méthode de classe `Song.from_obj()`.
    - Cela devrait lancer une exception de type `ValueError` car l'objet ne contient pas les champs nécessaires.
    - Il faut utiliser un mécanisme `try: ... except: ...` pour capturer l'exception `ValueError` et afficher le message de l'exception précédée de la chaîne `"ValueError, message:"`.
- Instancier une `Song` à partir de la 1ère chanson du fichier "data/songs.json".
    - Faites appel à la méthode de classe `Song.from_obj()`.
    - On peut utiliser l'instruction ci-bas pour obtenir le 1er objet d'un fichier JSON:
    ```Python
    first_data = json.load(open("data.json"))[0]
    ```
    - Afficher l'instance en la passant directement à la fonction `print()`.

Sortie attendue à l'appel de la fonction `testSong()` :
```plaintext
=============================== Tests partie 2.2 ===============================
Titre: Title
 Artiste: Artist
 Annee de sortie: 2024
 Instrument: Drum(brand='brand')
ValueError, message: Impossible d'instancier une chanson depuis l'objet '{}'.
Titre: Stan
 Artiste: Eminem ft. Dido
 Annee de sortie: 2000
 Instrument: Piano(brand='Yamaha')
```

### 2.3 Implémenter et tester `Playlist`
Pour cette section :
- l'implémentation ([2.3.1.](#231-définir-le-constructeur), [2.3.2.](#232-définir-les-méthodes-de-classe), [2.3.3.](#233-configurer-laccès-public-aux-attributs-privés-getters-et-setters), [2.3.4.](#234-surcharger-les-opérateurs-magiques), [2.3.5.](#235-définir-la-méthode-play_all)) se fait dans le fichier `modules/playlist.py` ;
- les tests ([2.3.6.](#236-tester-limplémentation)) se font dans la fonction `testPlaylist()` du fichier `main.py` ;
- lorsque vous avez terminé les instructions ci-bas, exécutez `main.py` à partir du dossier `part2/` pour voir la sortie de vos tests.

#### Description des attributs de `Playlist` :
| Attribut | Type | Description  | Contrainte |
| --- | --- | --- | --- |
| `__name` | `str` | *Attribut privé* : le nom de la `Playlist`. | `__name` commence  toujours par le préfix "Playlist-". |
| `__songs` | `dict[str,Song]` | *Attribut privé* : les `Song` que contient la `Playlist`. | `__songs` est un dictionnaire dont les clés sont les titres de chaque `Song`, et la valeur associée à chaque clé est l'instance de  `Song` correspondante. |

#### 2.3.1. Définir le constructeur
- La signature du constructeur est `__init__(self, name: str, songs: list[Song])`.
    - La valeur de `name` est utilisée pour initialiser l'attribut privé `__name`.
    - La liste de `Song` dans `songs` est utilisée pour initialiser l'attribut privé `__songs` qui est un dictionnaire.
    - Par convention le double *underscore* définie un attribut privé ; attribut non accessible depuis l'extérieur de la classe `Playlist`.

**Les contraintes sur les attributs présentées dans [ce tableau](#description-des-attributs-de-playlist-) doivent être respectées lors de l'initialisation**.

#### 2.3.2. Définir les méthodes de classe
Nous voulons pouvoir construire une instance de `Playlist` depuis un fichier CSV ou un fichier JSON contenant les informations de chansons. Pour cela, nous allons définir 2 méthodes de classes.

##### 2.3.2.1. Définir une méthode de classe pour la construction à partir d'un CSV
- La signature de cette méthode est `from_csv(cls, name: str, csv_path: str)`.
    - Le paramètre `name` contient le nom de la `Playlist`.
    - Le paramètre `csv_path` contient le chemin vers le fichier CSV.
- Utiliser un décorateur pour définir la méthode comme méthode de classe.
- Ouvrir le fichier se trouvant à `csv_path`.
    - Utiliser chaque ligne du fichier afin d'instancier une chanson via la méthode de classe `Song.from_obj()`.
    - Ajouter cette instance à une liste de `Song`.
- Instancier une `Playlist` en appelant son constructeur avec l'instruction `cls(...)` (remplacer les ... par le nom de la playlist et la liste de `Song` que vous venez de remplir).
- Retourner l'instance de `Playlist` que vous venez de construire.

##### 2.3.2.2. Définir une méthode de classe pour la construction à partir d'un JSON
- La signature de cette méthode est `from_json(cls, name: str, json_path: str)`.
    - Le paramètre `name` contient le nom de la `Playlist`.
    - Le paramètre `json_path` contient le chemin vers le fichier CSV.
- Utiliser un décorateur pour définir la méthode comme méthode de classe.
- Ouvrir le fichier se trouvant à `json_path`.
    - Utiliser chaque objet du fichier afin d'instancier une chanson via la méthode de classe `Song.from_obj()`.
    - Ajouter cette instance à une liste de `Song`.
- Instancier une `Playlist` en appelant son constructeur avec l'instruction `cls(...)` (remplacer les ... par le nom de la playlist et la liste de `Song` que vous venez de remplir).
- Retourner l'instance de `Playlist` que vous venez de construire.

#### 2.3.3. Configurer l'accès public aux attributs privés (*getters* et *setters*)
Comme pour la classe `Song` : nous allons définir des *getters* et des *setters* en utilisant respectivement les décorateurs `@property` et `@<attribute-name>.setter`.

Liste des ***getters*** à implémenter :
- `name(self) -> str` : retourne le nom de la `Playlist` dans une *string*.
- `songs(self) -> dict[str, Song]` : retoure les `Song` de la `Playlist` dans un dictionnaire.

Liste des ***setters*** à implémenter :
- `name(self, name: str)` : utilise la valeur de `name` pour initialiser le nom de la playlist.
- `songs(self, songs: list[Song])` : utilise la liste de `songs` pour initialiser les chansons de la playlist (contenues dans un dictionnaire).

**Les contraintes sur les attributs présentées dans [ce tableau](#description-des-attributs-de-playlist-) doivent être respectées lors de l'initialisation via ces setters**.

#### 2.3.4. Surcharger les opérateurs magiques
En Python, les opérateurs ou méthodes magiques (aussi appelée *dunder methods*) sont des méthodes spéciales qui commencent et se terminent par un double *underscore*. Elles ne sont pas censées être appelées explicitement dans le programme, leur invocation se produit en interne depuis la classe lors d'une action spécifique.

Dans les sections précédentes, vous les avez déjà rencontrées :
- `__repr__` de la classe `Instrument` et `__str__` de la classe `Song` ;
- ces opérateurs nous ont permis de manipuler la représentation textuelle de nos instances lors d'un appel à `print()`.

Dans cette section, notre but est de surcharger les opérateurs `__iter__`, `__add__` et `__sub__` de la classe `Playlist`.

##### 2.3.4.1. Surcharger l'opérateur `__iter__()`
Le but est de pouvoir itérer sur une `Playlist` en utilisant une boucle de la forme suivante :
```Python
for song in playlist:
    # Faire quelque chose
```
- où `playlist` est une instance de `Playlist`, et `song` est une instance de `Song`.

Nous devons surcharger l'opérateur dont la signature est `__iter__(self) -> Iterator[Song]`. Pour l'implémenter il faut :
- Transformer le dictionnaire `__songs` de la `Playlist` en une liste de `Song`.
- Appeler explicitement l'opérateur `__iter__()` sur la liste.
- Retourner ce que l'appel à `__iter__()` sur la liste vous donne.

##### 2.3.4.2. Surcharger l'opérateur `__add__()`
Le but est de pouvoir ajouter une chanson dans une `Playlist` avec l'opérateur `+` :
```Python
playlist += song
# ou
playlist = playlist + song
```
- où `playlist` est une instance de `Playlist` et `song` est une instance de `Song`.

Nous devons surcharger l'opérateur dont la signature est ` __add__(self, song: Song)` (le paramètre `song` est la chanson à ajouter). Pour l'implémenter il faut :
- Vérifier si la chanson passée en paramètre est une instance de type `Song`.
    - Si oui :
        - Ajouter la chanson dans le dictionnaire `__songs`.
        - Retourner l'instance de `Playlist` sur laquelle l'opérateur `+` a été appelé.
    - Sinon: 
        - Lever une exception `TypeError` et passer le message suivant :
        ```Python
        "Impossible d'ajouter une chanson de type <type-du-paramètre-song>."
        ```

##### 2.3.4.3. Surcharger l'opérateur `__sub__()`
Le but est de pouvoir retirer la chanson d'une `Playlist` avec l'opérateur `-` :
```Python
playlist -= song.title
# ou
playlist = playlist - song.title
```
- où `playlist` est une instance de `Playlist` et `song` est une instance de `Song`.

Nous devons surcharger l'opérateur dont la signature est `__sub__(self, song_title: str)` (le paramètre `song_title` est le titre de la chanson à retirer). Pour l'implémenter il faut :
- Si la chanson `song_title` est dans la `Playlist`, retirer la chanson du dictionnaire `__songs`.
- Retourner l'instance de `Playlist` sur laquelle l'opérateur `-` a été appelé.

#### 2.3.5. Définir la méthode `play_all()`
Cette méthode simule le fait de jouer toutes les chansons de la playlist à partir de leur instrument respectif par l'affichage d'un message.

On peut jouer une playlist en commençant par la 1ère chanson, ou en mode aléatoire (l'ordre de chaque chanson est choisi de manière aléatoire).
- La signature de cette méthode est `play_all(self, rdm_mode: bool=False)` : le paramètre `rdm_mode` indique si on joue la playlist en mode aléatoire.
- (Au tout début) La méthode doit afficher le nom de la playlist et le nombre de chansons qu'elle contient ainsi :
    ```Python
    "Lecture de <nom-de-la-playlist> (<nombre-de-chansons> chansons en mode <mode-de-lecture>)"
    ```
    - `<mode-de-lecture>` correspond à la *string* "standard" si `rdm_mode` est `False`, et "aléatoire" sinon.
- La méthode doit faire appel à la méthode `play()` de chacune de ses chansons.
- Si le mode aléatoire est choisi on doit déterminer l'ordre de lecture de chaque chanson aléatoirement.
    - Conseils :
        - Utiliser la structure de données ensemble (*set* en anglais).
        - Utiliser la méthode `random.choice()` (de la librairie `random`).

#### 2.3.6. Tester l'implémentation
Compléter la fonction `testPlaylist()` de `main.py`:
- Instancier une `Playlist` nommée "Playlist-csv" depuis le fichier CSV `data/songs.csv`.
    - Faites appel à la méthode de classe `Playlist.from_csv()`.
- Instancier une `Playlist` nommée "Playlist-json" depuis le fichier JSON `data/songs.json`.
    - Faites appel à la méthode de classe `Playlist.from_json()`.
- Ajouter un dictionnaire/objet vide (i.e. {}) à la playlist "Playlist-json".
    - Faites appel à l'opérateur `+`.
    - Cela devrait lancer une exception de type `TypeError` car l'objet ajouté n'est pas de type `Song`.
    - Utiliser un mécanisme `try: ... except: ...` pour capturer l'exception `TypeError` et afficher le message de l'exception précédée de la chaîne `"TypeError, message:"`.
- Ajouter les chansons de la playlist "Playlist-json" à la playlist "Playlist-csv".
    - Pour itérer, vous devez utiliser une boucle de la forme `for song in playlist` (c.f. section [2.3.4.1.](#2341-surcharger-lopérateur-__iter__)).
    - Faites appel à l'opérateur `+`.
- Retirer la chanson intitulée "We Will Rock You" de la playlist "Playlist-csv" en appelant l'opérateur `-`.
- Jouer toutes les chansons de la playlist "Playlist-json" en mode normal.
- Jouer toutes les chansons de la playlist "Playlist-csv" en mode aléatoire.

Sortie attendue à l'appel de la fonction `testPlaylist()` :
```plaintext
=============================== Tests partie 2.3 ===============================
TypeError, message: Impossible d'ajouter une chanson de type <class 'dict'>.
Lecture de Playlist-json (5 chansons en mode standard)
Joue Stan                      solo avec *** piano ***    du fabricant Yamaha
Joue In the End                solo avec *** piano ***    du fabricant Korg
Joue We Will Rock You          solo avec *** batterie *** du fabricant Ludwig
Joue Rolling in the Deep       solo avec *** piano ***    du fabricant Bösendorfer
Joue Take Me to Church         solo avec *** piano ***    du fabricant Roland
Lecture de Playlist-csv (9 chansons en mode aléatoire)
Joue In the End                solo avec *** piano ***    du fabricant Korg
Joue Eye of the Tiger          solo avec *** batterie *** du fabricant Pearl
Joue Billie Jean               solo avec *** batterie *** du fabricant Yamaha
Joue The Next Episode          solo avec *** guitare ***  du fabricant Music Man
Joue Smells Like Teen Spirit   solo avec *** guitare ***  du fabricant Fender
Joue Take Me to Church         solo avec *** piano ***    du fabricant Roland
Joue Rolling in the Deep       solo avec *** piano ***    du fabricant Bösendorfer
Joue Stan                      solo avec *** piano ***    du fabricant Yamaha
Joue My Heart Will Go On       solo avec *** piano ***    du fabricant Steinway
```
Note : la lecture aléatoire de "Playlist-csv" ne produira pas forcément une sortie identique, mais vous pouvez vous assurez visuellement que l'appel joue 9 chansons différentes et que "We Will Rock You" ne se trouve pas dans la liste.
