from typing import List
class Song:
    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

class PlayList:
    def __init__(self):
        #self.__plylist: List[Song] = [] # so instead of List i will use set
        self.__plylist: set[Song] = set()

    def add_song(self, song: Song):
        self.__plylist.add(song)

    def get_playlist(self) -> List[Song]:
        return self.__plylist

playlist = PlayList()
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
playlist.add_song(Song("Song 4"))

# Now the problem is that we are using set instead of list so the order of the songs is not maintained and also 
# we cannot access the songs by index so we will use list instead of set

#  The client needs to know the type of the collection and also the client needs to know the implementation of the collection 
# so we will use iterator design pattern to solve this problem
for i in range(len(playlist.get_playlist())):
    print(playlist.get_playlist()[i].get_title())




