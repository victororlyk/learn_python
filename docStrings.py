class Song:
    """
    class to represent a song
    """

    def __init__(self, title, artist, duration=0):
        """
        :param title: (str) Initialises the 'title' attribute
        :param article: (Artist) At  Artist object represeting the song's
        creator.
        :param duration:(Optional[int]) Initial value for the 'duration'
                attribute. Will defualt to zero if not specified.
        """
        self.title = title
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
        :param song:  a song to add
        :param position: optional[int] if specified the song will be added
        to that position, otherwise to the end of the list
        :return: None
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt", "r", encoding='utf-8') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we'be just read details for a new artist retireve artist
                # object if there is one
                # otherweise create a new artist object and add it to the
                # artist line
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # we'be just read a new album for the current artist
                # retrieve the album object if there is one
                # otherwise create a new album object and o=sotre it in athe
                # artists collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)
            # create a new song object and add it to the current albums's
            # collections
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    with open('checkfile.txt', "w", encoding='utf-8') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(
                        new_artist, new_album, new_song), file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    create_checkfile(artists)
