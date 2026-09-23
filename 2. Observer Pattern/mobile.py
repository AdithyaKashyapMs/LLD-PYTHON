from observer import Observer

# Let's create a MobileDisplay class that implements the Observer interface
# so we dont need to add it in weather_station.py file. We can just import it and use it in main.py file.
class MobileDisplay(Observer):
    def update(self, temp: int):
        print(f"Mobile temperature: {temp}")