from abc import ABC, abstractmethod


# Abstract Product A
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# Abstract Product A
class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# Concreate Product A1
class LightButton(Button):
    def render(self) -> str:
        return "Rendering Light theme Button"


# Concreate Product A2
class DarkButton(Button):
    def render(self) -> str:
        return "Rendering Dark theme Button"


# Concreate Product B1
class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Light theme Checkbox"


# Concreate Product B2
class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering Dark theme Checkbox"


# Abstract Factory
class ThemeFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factory 1
class LightThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


# Concrete Factory 2
class DarkThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


def client_code(factory: ThemeFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


client_code(LightThemeFactory())
client_code(DarkThemeFactory())
