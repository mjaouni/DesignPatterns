from abc import ABC, abstractmethod


class Document(ABC):
    def generate(self):
        self.create_header()
        self.create_body()
        self.create_footer()

    def create_header(self):
        print("Creating a standard document header")

    @abstractmethod
    def create_body(self):
        pass

    def create_footer(self):
        print("Creating a standard document footer")


# Concrete Classes

class Report(Document):
    def create_body(self):
        print("Writing the report content with analysis and findings.")


class Invoice(Document):
    def create_body(self):
        print("Writing the invoice content with itemized billing details.")


# Usage

report = Report()
report.generate()
print()

invoice = Invoice()
invoice.generate()

