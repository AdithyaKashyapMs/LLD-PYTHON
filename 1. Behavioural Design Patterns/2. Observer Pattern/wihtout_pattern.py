## Tightly coupled implementation of Observer Pattern
# weather and display are tightly coupled, which makes it difficult to modify or extend the code in the future.

class PhoneDisplay:
    def update(self, new_temp):
        print(f"Phone display: The temperature is now {new_temp} degrees.")

# But now if we want to add another display, we would have to modify the WeatherStation class, which violates the Open/Closed Principle
class LaptopDisplay:
    def update(self, new_temp):
        print(f"Laptop display: The temperature is now {new_temp} degrees.")

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_display = PhoneDisplay()
        self.__laptop_display = LaptopDisplay()

    def update_temperature(self, new_temp):
        self.__temperature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update(self.__temperature)
        # If we want to add another display, we would have to modify this method, which violates the Open/Closed Principle
        self.__laptop_display.update(self.__temperature)

w = WeatherStation()
w.update_temperature(30)