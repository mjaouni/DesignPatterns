from abc import ABC, abstractmethod


# Abstract State
class VendingMachineState(ABC):

    @abstractmethod
    def insert_coin(self, vending_machine: 'VendingMachine'):
        pass

    @abstractmethod
    def eject_coin(self, vending_machine: 'VendingMachine'):
        pass

    @abstractmethod
    def press_button(self, vending_machine: 'VendingMachine'):
        pass

    @abstractmethod
    def dispense(self, vending_machine: 'VendingMachine'):
        pass


# Concreate States
class NoCoinState(VendingMachineState):
    def insert_coin(self, vending_machine: 'VendingMachine'):
        print('Coin Inserted.')
        vending_machine.state = HasCoinState()

    def eject_coin(self, vending_machine: 'VendingMachine'):
        print('No coin to eject.')

    def press_button(self, vending_machine: 'VendingMachine'):
        print("No coin inserted ,can't press the button.")

    def dispense(self, vending_machine: 'VendingMachine'):
        print("No coin inserted ,can't dispense any item.")


class HasCoinState(VendingMachineState):
    def insert_coin(self, vending_machine: 'VendingMachine'):
        print("Coin already inserted.")

    def eject_coin(self, vending_machine: 'VendingMachine'):
        print("Coin ejected.")
        vending_machine.state = NoCoinState()  # This line is crucial for the state transition

    def press_button(self, vending_machine: 'VendingMachine'):
        print("Button Pressed.")
        vending_machine.state = DispensingState()
        vending_machine.dispense()

    def dispense(self, vending_machine: 'VendingMachine'):
        print("Press the button to dispense the item.")


class DispensingState(VendingMachineState):
    def insert_coin(self, vending_machine: 'VendingMachine'):
        print("Please wait,dispensing the item.")

    def eject_coin(self, vending_machine: 'VendingMachine'):
        print("Item is being dispensed,can't eject the coin.")

    def press_button(self, vending_machine: 'VendingMachine'):
        print("Item is already being dispensed.")

    def dispense(self, vending_machine: 'VendingMachine'):
        print("Dispensing item...")
        if vending_machine.item_count > 1:
            vending_machine.item_count -= 1
            vending_machine.state = NoCoinState()
        else:
            vending_machine.item_count -= 1
            print("Out of Items.")
            vending_machine.state = SoldOutState()


class SoldOutState(VendingMachineState):
    def insert_coin(self, vending_machine: 'VendingMachine'):
        print('Cannot insert coin.The machine is sold out.')

    def eject_coin(self, vending_machine: 'VendingMachine'):
        print("Cannot eject coin. No coin inserted.")

    def press_button(self, vending_machine: 'VendingMachine'):
        print("Cannot press button.No Coin inserted ,the machine is sold out.")

    def dispense(self, vending_machine: 'VendingMachine'):
        print("Cannot dispense.The machine is sold out.")


# Vending Machine (Context)
class VendingMachine:
    def __init__(self, item_count):
        self.item_count = item_count
        if item_count > 0:
            self.state = NoCoinState()
        else:
            self.state = SoldOutState()

    def insert_coin(self):
        self.state.insert_coin(self)

    def eject_coin(self):
        self.state.eject_coin(self)

    def press_button(self):
        self.state.press_button(self)

    def dispense(self):
        self.state.dispense(self)

    def __str__(self):
        return f"Vending Machine [Item Count:{self.item_count}, Current State: {self.state.__class__.__name__}]"


# Usage

vending_machine = VendingMachine(3)

print(vending_machine)

vending_machine.insert_coin()
print(vending_machine)

vending_machine.press_button()
print(vending_machine)

vending_machine.insert_coin()
vending_machine.eject_coin()
print(vending_machine)

vending_machine.insert_coin()
vending_machine.press_button()
print(vending_machine)

vending_machine.insert_coin()
vending_machine.press_button()
print(vending_machine)

vending_machine.insert_coin()
print(vending_machine)

