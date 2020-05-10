import os
import fnmatch
import id3reader_p3 as id3reader


def get_all(path: str, extension: str):
    for path, directories, files in os.walk(path):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


my_music = get_all('music', 'emp3')
error_list = []

for f in my_music:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Albums:{}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except OSError:
        error_list.append(f)
        continue
print(error_list)
