from typing import List
from abc import ABC, abstractmethod

class Song:
    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

# First we will do an abstract class for the iterator which will be implemented by the concrete iterator
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Song:
        pass
# if we want to implement the another iterator for the same collection 
# such as linked list or set etc we need to implement the 
# same interface for the new iterator and we can use the same collection for the new iterator
# client should not know about the implementation of the collection and the iterator 
# so we will use the iterator design pattern to solve this problem

class PlayListIterator(Iterator):
    def __init__(self, song_list: List[Song]):
        self.__song_list = song_list
        self.__position = 0

    def has_next(self) -> bool:
        if self.__position < len(self.__song_list):
            return True
        return False

    def next(self) -> Song | None:
        # Corrected: Access list element using [] instead of ()
        if self.has_next(): # Check has_next before accessing to prevent IndexError
            song = self.__song_list[self.__position]
            self.__position += 1
            return song
        return None

class Playlist:
    def __init__(self):
        self.__playlist: List[Song] = []

    def add_song(self, song: Song):
        self.__playlist.append(song)

    def create_iterator(self) -> PlayListIterator:
        return PlayListIterator(self.__playlist)

playlist = Playlist()
# Corrected: Pass Song objects instead of strings
playlist.add_song(Song("Song 1"))
playlist.add_song(Song("Song 2"))
playlist.add_song(Song("Song 3"))
playlist.add_song(Song("Song 4"))

iterator = playlist.create_iterator()

while iterator.has_next():
    print(iterator.next().get_title())