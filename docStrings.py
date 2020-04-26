class Song:
    """
    class to represent a song

    Attributes:
        title:(str): the title of the song
        artist(Artist): An artist object representing the songs creator
        duration(int): the duration of the song in second. May be zero
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
