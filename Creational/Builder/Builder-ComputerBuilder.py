from abc import ABC, abstractmethod


# Product class representing the object being built
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphic_card = None
        self.operating_system = None

    def __str__(self):
        return (f'CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, Graphics Card: {self.graphics_card},'
                f' OS: {self.operating_system}')


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_ram(self, cpu):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def set_graphic_card(self, graphic_card):
        pass

    @abstractmethod
    def set_operating_system(self, operating_system):
        pass

    @abstractmethod
    def get_computer(self):
        pass


# GamingComputerBuilder:Concreate of ComputerBuilder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def set_graphic_card(self, graphic_card):
        self.computer.graphics_card = graphic_card

    def set_operating_system(self, operating_system):
        self.computer.operating_system = operating_system

    def get_computer(self):
        return self.computer


# WorkstationComputerBuilder:Concreate of ComputerBuilder
class WorkstationComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def set_graphic_card(self, graphic_card):
        self.computer.graphics_card = graphic_card

    def set_operating_system(self, operating_system):
        self.computer.operating_system = operating_system

    def get_computer(self):
        return self.computer


# Gaming Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_gaming_computer(self):
        self.builder.set_cpu('Intel i9')
        self.builder.set_ram('32GB')
        self.builder.set_storage('1TB SSD')
        self.builder.set_graphic_card('NVIDIA RTX 3080')
        self.builder.set_operating_system('Windows 10')

    def construct_workshop_computer(self):
        self.builder.set_cpu('Intel i11')
        self.builder.set_ram('100GB')
        self.builder.set_storage('5TB SSD')
        self.builder.set_graphic_card('NVIDIA RTX 7000')
        self.builder.set_operating_system('Linux')


# Usage
if __name__ == "__main__":
    GamingBuilder = GamingComputerBuilder()
    director = Director(GamingBuilder)
    director.construct_gaming_computer()
    gaming_computer = GamingBuilder.get_computer()
    print(gaming_computer)

    WorkstationBuilder = WorkstationComputerBuilder()
    director = Director(WorkstationBuilder)
    director.construct_workshop_computer()
    workshop_computer = WorkstationBuilder.get_computer()
    print(workshop_computer)
