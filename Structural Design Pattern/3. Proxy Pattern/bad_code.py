import time 

class HighResolutionImage:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__image_data = None

        self._load_from_disk()  # Load the image data from disk when the object is created

    def _load_from_disk(self):
        time.sleep(1)
        self.__image_data = f"[Load[ed image data of {self.__file_name}]]"
        print(f"Loaded image from disk: {self.__file_name}")

    def display(self):
        print(f"Displaying image: {self.__file_name} with data: {self.__image_data}")

class PhotoGallery:
    def __init__(self):
        self.__images: list[HighResolutionImage] = []

    def add_image(self, file_name: str):
        image = HighResolutionImage(file_name)
        self.__images.append(image)

    def display_gallery(self):
        for image in self.__images:
            image.display()

# Here comes the main part of the code
photo_gallery = PhotoGallery()
# Adding images to the gallery
photo_gallery.add_image("image1.jpg")
photo_gallery.add_image("image2.jpg")
photo_gallery.add_image("image3.jpg")
photo_gallery.add_image("image4.jpg")

# I will first only load images before displaying them. This is because loading images from disk is a time-consuming operation, and we want to avoid loading all images at once. Instead, we will load images only when they are needed for display.
# It is taking time to load but i have not even dispaled 
# Every time we add the imge the image is loaded from disk and it takes time. So, we need to use a proxy pattern to avoid loading the image from disk until it is actually needed for display.
# Bad example the image should be loaded only when it is actually needed for display. But in this case, the image is loaded from disk as soon as it is added to the gallery. This is not efficient because loading images from disk is a time-consuming operation, and we want to avoid loading all images at once. Instead, we will load images only when they are needed for display.
# photo_gallery.display_gallery()