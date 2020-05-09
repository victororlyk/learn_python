import os

root = 'music'
for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        print("*" * 40)
        for f in files:
            song_details = f[:-5].split(" - ")
            print(song_details)
        print("*" * 40)
    # print(path)
    # print(directories)
    # print(files)
    # print()
    # for f in files:
    #     print("\t{}".format(f))
