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


class ImageProxy:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__real_image = None

    def display(self):
        if self.__real_image is None:
            self.__real_image = HighResolutionImage(
                self.__file_name
            )  # Load the image from disk only when it is needed for display
        self.__real_image.display()


class PhotoGallery:
    def __init__(self):
        self.__images: list[ImageProxy] = []

    def add_image(self, file_name: str):
        image_proxy = ImageProxy(file_name)
        self.__images.append(image_proxy)

    def display_gallery(self):
        for image in self.__images:
            image.display()

    def show_image(self, index: int):
        self.__images[index - 1].display()


start_time = time.time()
photo_gallery = PhotoGallery()
photo_gallery.add_image("image1.jpg")
photo_gallery.add_image("image2.jpg")
photo_gallery.add_image("image3.jpg")
photo_gallery.add_image("image4.jpg")
end_time = time.time()
print(f" {end_time - start_time:.1f} seconds")

photo_gallery.show_image(2)  # Display the second image in the gallery
