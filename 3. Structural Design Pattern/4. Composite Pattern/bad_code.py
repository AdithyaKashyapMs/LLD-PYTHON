from typing import List
class File:
    def __init__(self, name: str):
        self.__name = name
    
    def show_details(self):
        return f"File: {self.__name}"

class Folder:
    def __init__(self, name: str):
        self. __name = name
        self.__files: List[File]= []
    
    def add_file(self, file: File):
        self.__files.append(file)

    def show_details(self):
        print(f"Folder: {self.__name}")
        for file in self.__files:
            print(file.show_details())

file1 = File("file1.txt")
file2 = File("file2.txt")
file3 = File("file3.txt")

folder1 = Folder("Folder1")
folder1.add_file(file1)
folder1.add_file(file2)
folder1.add_file(file3)

folder1.show_details()

# Now if we want to add a folder inside a folder, we can create a new class called SubFolder that inherits from the Folder class and implements the same methods as the Folder class. This way, we can add a SubFolder inside a Folder and still be able to show the details of the SubFolder and its files.
# How to differentiate between a file and a folder? We can create a new class called FileSystemObject that has a method called show_details() and then make the File and Folder classes inherit from the FileSystemObject class. This way, we can treat both files and folders as FileSystemObjects and call the show_details() method on them without worrying about whether they are files or folders.
# but composite pattern says we need to handle both files and folders in the same way. So, we can create a new class called FileSystemObject that has a method called show_details() and then make the File and Folder classes inherit from the FileSystemObject class. This way, we can treat both files and folders as FileSystemObjects and call the show_details() method on them without worrying about whether they are files or folders.
