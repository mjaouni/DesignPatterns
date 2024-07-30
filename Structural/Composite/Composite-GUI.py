from abc import ABC, abstractmethod
from typing import List


# Component Abstract Interface
class GUIElement(ABC):
    @abstractmethod
    def render(self):
        pass


# Button: Leaf Concreate GUIElement
class Button(GUIElement):
    def __init__(self, label: str):
        self.label = label

    def render(self):
        print(f'Button [{self.label}]')


# TextField: Leaf Concreate GUIElement
class TextField(GUIElement):
    def __init__(self, text: str):
        self.text = text

    def render(self):
        print(f'TextField [{self.text}]')


# Composite
class Panel(GUIElement):
    def __init__(self, name):
        self.name = name
        self.elements: List[GUIElement] = []

    def add_element(self, element: GUIElement):
        self.elements.append(element)

    def remove_element(self, element: GUIElement):
        self.remove_element(element)

    def render(self):
        print(f"Panel: {self.name}")
        for element in self.elements:
            element.render()


# Usage
button = Button('Submit')
button_cancel = Button('Cancel')

text_field = TextField('Enter your Name')

panel = Panel('Form')
panel.add_element(button)
panel.add_element(button_cancel)
panel.add_element(text_field)

button_back = Button('Back')

main_panel = Panel('Main')
main_panel.add_element(panel)
main_panel.add_element(button_back)

main_panel.render()
