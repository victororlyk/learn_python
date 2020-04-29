class Song:
    """
    class to represent a song
    """

    def __init__(self, name, artist, duration=0):
        """
        :param name: (str) Initialises the 'title' attribute
        :param artist: (Artist) At  Artist object represeting the song's
        creator.
        :param duration:(Optional[int]) Initial value for the 'duration'
                attribute. Will defualt to zero if not specified.
        """
        self.name = name
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an Album, using it's track list

    Methods:
        add_song: used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        """
        :param name:  the album name
        :param year: the year album was created
        :param artist: the artist reponsive foe the album.
        :param tracks: List[Song]
        """
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list
        :param song:  a title of song to add
        :param position: optional[int] if specified the song will be added
        to that position, otherwise to the end of the list
        :return: None
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """
    Basic class to sto reartist details
    Methods:
        add_album: use to add a new album
    """

    def __init__(self, name):
        """
        :param name: str
        :param albums: List(Album)
        """
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        :param album:(Album) if album is present it will not be added to the string
        :return: None
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """
        Add a new song to the collection of albums
        :param name: name of the album
        :param year: the year album was produced
        :param title: title of the song
        :return: None
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print("{} not found".format(name))
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album {}".format(name))
        album_found.add_song(title)


def find_object(field, object_list):
    """
    :param field: name
    :param object_list:  check if it has field param in it
    :return: field
    """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r", encoding='utf-8') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    with open('checkfile.txt', "w", encoding='utf-8') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(
                        new_artist, new_album, new_song), file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    create_checkfile(artists)
