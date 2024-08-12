from abc import ABC, abstractmethod


# Abstract Class
class DataProcessor(ABC):
    def process_data(self):
        self.read_data()
        self.process_steps()
        self.save_data()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    def process_steps(self):
        print('Processing data ...')  # Common processing step


# Concrete Classes
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from CSV file")

    def save_data(self):
        print("Saving data to CSV file")


class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from JSON file")

    def save_data(self):
        print("Saving Data to JSON file")


# Usage
csv_processor = CSVDataProcessor()
csv_processor.process_data()

print()

json_processor = JSONDataProcessor()
json_processor.process_data()
