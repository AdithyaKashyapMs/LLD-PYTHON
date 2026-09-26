from typing import List
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name
    
    def show_details(self):
        return f"File: {self.__name}"

class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self. __name = name
        self.__components: List[FileSystemComponent] = []
    
    def add_component(self, component: FileSystemComponent):
        self.__components.append(component)

    def show_details(self):
        print(f"Folder: {self.__name}")
        for component in self.__components:
            print(component.show_details())

file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

sub_folder = Folder("SubFolder")
sub_folder.add_component(file1)
sub_folder.add_component(file2)
sub_folder.add_component(file3)

image_file = File("image.png")
movie_file = File("movie.mp4")

main_folder = Folder("MainFolder")
main_folder.add_component(image_file)
main_folder.add_component(movie_file)
main_folder.add_component(sub_folder)

main_folder.show_details()

# Keep in mind if there is a hierarchy structure then we can use the composite pattern to represent the hierarchy structure. 
# The composite pattern allows us to treat individual objects and compositions of objects uniformly. In this example,
# we have a folder that can contain files and other folders, and we can treat them all as FileSystemComponents. 
# This way, we can call the show_details() method on any FileSystemComponent without worrying about whether it is a file or a folder.