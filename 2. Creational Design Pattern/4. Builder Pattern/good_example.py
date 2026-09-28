class Laptop:
    processor = None
    ram = None
    graphics_card = None
    color = None
    display_size = None

    def display_specs(self):
        if self.processor:
            print(f"Processor: {self.processor}")
        if self.ram:
            print(f"RAM: {self.ram}")
        if self.graphics_card:
            print(f"Graphics Card: {self.graphics_card}")
        if self.color:
            print(f"Color: {self.color}")
        if self.display_size:
            print(f"Display Size: {self.display_size}")


class LaptopBuilder:
    def __init__(self):
        self.__laptop = Laptop()

    def set_processor(self, processor: str):
        self.__laptop.processor = processor
        return self

    def set_ram(self, ram: str):
        self.__laptop.ram = ram
        return self

    def set_graphics_card(self, graphics_card: str):
        self.__laptop.graphics_card = graphics_card
        return self

    def set_color(self, color: str):
        self.__laptop.color = color
        return self

    def set_display_size(self, display_size: str):
        self.__laptop.display_size = display_size
        return self

    def build(self):
        return self.__laptop


# This is method chaining. We can chain the methods of the LaptopBuilder 
# class to set the properties of the Laptop object and then call the build() method to get the final Laptop object.

# we do not need to pass all the parameters to the constructor of the Laptop class. We can set only the properties that we want to set and leave the rest as None. 
# This makes the code more readable and maintainable.
l = LaptopBuilder().set_processor("i5-34343").set_ram("16GB").set_color("Green").build()  # noqa: E741
l.display_specs()