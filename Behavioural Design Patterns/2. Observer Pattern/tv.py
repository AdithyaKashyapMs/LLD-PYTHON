from observer import Observer

class TVDisplay(Observer):
    def update(self, temp: int):
        print(f"TV temperature: {temp}")