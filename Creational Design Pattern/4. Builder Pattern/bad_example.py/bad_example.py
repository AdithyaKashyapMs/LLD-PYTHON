class Laptop:
    def __init__(
                self, 
                processor: str,
                ram: str,
                graphics_card: str = None,
                color: str = None,
                display_size: str = None
                ):
        
        self.processor = processor
        self.ram = ram
        self.graphics_card = graphics_card
        self.color = color
        self.display_size = display_size

    def display_specs(self):
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram}")
        if self.graphics_card:
            print(f"Graphics Card: {self.graphics_card}")
        if self.color:
            print(f"Color: {self.color}")
        if self.display_size:
            print(f"Display Size: {self.display_size}")

laptop1 = Laptop("Intel i7", "16GB")
laptop1.display_specs()

# Notice the problem here if the contructor has too many parameters, 
# it becomes difficult to remember the order of the parameters and it can lead to errors.
laptop2 = Laptop("AMD Ryzen 9", "32GB", None, "Silver", None)
laptop2.display_specs()