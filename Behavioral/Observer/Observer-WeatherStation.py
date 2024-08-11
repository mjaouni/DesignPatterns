from abc import ABC, abstractmethod


# Subject(Publisher) Interface
class Publisher(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concreate Subject(Publisher)
class WeatherStation(Publisher):
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify_observers()

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value
        self.notify_observers()

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value
        self.notify_observers()


# Observer Interface
class DisplayDevice(ABC):
    @abstractmethod
    def update(self, weather_station):
        pass


# Concreate Observers
class PhoneApp(DisplayDevice):
    def update(self, weather_station: Publisher):
        print(
            f'Phone App:Weather updated - Temperature :{weather_station.temperature}, Humidity : {weather_station.humidity},Pressure :{weather_station.pressure} ')


class Website(DisplayDevice):
    def update(self, weather_station: Publisher):
        print(
            f'Website:Weather updated - Temperature :{weather_station.temperature}, Humidity : {weather_station.humidity},Pressure :{weather_station.pressure} ')


class DigitalBillboard(DisplayDevice):
    def update(self, weather_station: Publisher):
        print(
            f'Digital Billboard:Weather updated - Temperature :{weather_station.temperature}, Humidity : {weather_station.humidity},Pressure :{weather_station.pressure} ')


# Usage
weather_station = WeatherStation()

# Create display devices
phone_app = PhoneApp()
website = Website()
digital_billboard = DigitalBillboard()

weather_station.register_observer(phone_app)
weather_station.register_observer(website)
weather_station.register_observer(digital_billboard)

weather_station.temperature = 25.0
weather_station.humidity = 60
weather_station.pressure = 1013

weather_station.temperature = 22.0
weather_station.humidity = 65
weather_station.pressure = 1010
