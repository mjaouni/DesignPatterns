from abc import ABC, abstractmethod
from typing import List


# Component :Abstract Interface
class Employee(ABC):
    def show_details(self):
        pass


# Developer: Leaf Concreate Employee
class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f'Developer name {self.name}, Position:{self.position}')


# Designer:Leaf Concreate Employee
class Designer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f'Designer name {self.name}, Position:{self.position}')


# Composite
class Team(Employee):
    def __init__(self, name):
        self.name = name
        self.members : List[Employee] = []

    def add_member(self, employee: Employee):
        self.members.append(employee)

    def remove_member(self, employee: Employee):
        self.members.remove(employee)

    def show_details(self):
        print(f'Team {self.name}')
        for member in self.members:
            member.show_details()


# Usage
# Leaf Objects

developer = Developer("Mohammad Jaouni", "Senior Software Engineer")

designer = Designer("Roro Roro", "UI/UX Designer")

team = Team('Xcoding')
team.add_member(developer)
team.add_member(designer)

team_holding = Team('Holding')
developer_holding = Developer("Hassan Hosni", "Senior Software Engineer")
team_holding.add_member(developer_holding)
team_holding.add_member(team)

team_holding.show_details()
