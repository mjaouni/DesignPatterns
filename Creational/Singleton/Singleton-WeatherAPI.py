import threading


class WeatherAPI:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(WeatherAPI, cls).__new__(cls)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.api_key = "your_api_key_here"  # Replace with your actual API key
        self.api_url = "http://api.weatherapi.com/v1/current.json"
        self.weather_data = None  # Store weather data lazily
        print("WeatherAPI instance created.")

    def get_weather(self, location):
        # Simulate fetching weather data
        if not self.weather_data:
            self.weather_data = {"location": location, "temperature": "20°C"}
        return self.weather_data


# Usage
weather_api1 = WeatherAPI()
weather_api2 = WeatherAPI()

print(weather_api1.get_weather("New York"))
print(weather_api1 is weather_api2)  # Output: True
