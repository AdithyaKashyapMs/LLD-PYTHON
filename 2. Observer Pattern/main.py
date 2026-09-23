from weather_station import WeatherStation
from tv import TVDisplay
from mobile import MobileDisplay

ws = WeatherStation()
tv = TVDisplay()

ws.add_observer(tv)

ws.update_temperature(25)
mobile = MobileDisplay()

# we dont need to modify the weather_station.py 
#  file to add the MobileDisplay class as an observer. We can just import it and use it in main.py file.
ws.add_observer(mobile)
ws.update_temperature(30)