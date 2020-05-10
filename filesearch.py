import os
import fnmatch
import id3reader._p3 as id3reader




def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        for artist in (d for d in directories if
                       fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


albums_list = find_albums("music", "Aerosmith")
song_list = find_songs(albums_list)


# for a in song_list:
#     print(a)


def get_all(path: str, extension: str):
    for path, directories, files in os.walk(path):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


# for f in get_all('music', 'emp3'):
#     print(f)
