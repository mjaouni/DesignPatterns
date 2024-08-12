import configparser


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._initialize_config()
        return cls._instance

    @classmethod
    def _initialize_config(cls):
        cls._instance.settings = configparser.ConfigParser()
        try:
            cls._instance.settings.read('config.properties')
        except Exception as e:
            print(f"Error loading configuration: {e}")

    def get(self, key, default_value=None):
        return self.settings.get('DEFAULT', key, fallback=default_value)


# Usage
config1 = Config()
config2 = Config()

print(config1.get('api_key', 'default_key'))
print(config1 is config2)  # Output: True
