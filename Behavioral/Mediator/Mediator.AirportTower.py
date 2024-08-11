from abc import ABC, abstractmethod


# Mediator interface

class AirTrafficControlMediator(ABC):

    @abstractmethod
    def notify(self, sender, event):
        pass


# ConcreteMediator
class ControlTower(AirTrafficControlMediator):
    def __init__(self):
        self._aircrafts = []

    def register_aircraft(self, aircraft):
        self._aircrafts.append(aircraft)

    def notify(self, sender, event):
        if event == 'ready_to_land':
            print(f'{sender.get_name()} is ready for landing')
            self.coordinate_landing(sender)

        elif event == 'ready_to_take_off':
            print(f'{sender.get_name()} is ready for takeoff')
            self.coordinate_takeoff(sender)

        elif event == 'landed':
            print(f'{sender.get_name()} has landed')

        elif event == 'took_off':
            print(f'{sender.get_name()} has taken off')

    def coordinate_landing(self, aircraft):
        for ac in self._aircrafts:
            if ac != aircraft and ac.is_landing():
                print(f'{aircraft.get_name()} must wait to land')
                return
        aircraft.land()

    def coordinate_takeoff(self, aircraft):
        for ac in self._aircrafts:
            if ac != aircraft and ac.is_take_off():
                print(f'{aircraft.get_name} must wait to takeoff')
                return
        aircraft.takeoff()


# Colleague
class Aircraft:
    def __init__(self, name, control_tower):
        self._name = name
        self._control_tower = control_tower
        self._is_landing = False
        self._is_takeoff = False
        self._control_tower.register_aircraft(self)

    def get_name(self):
        return self._name

    def is_landing(self):
        return self._is_landing

    def is_take_off(self):
        return self._is_takeoff

    def request_landing(self):
        self._is_landing = True
        self._control_tower.notify(self, 'ready_to_land')

    def request_takeoff(self):
        self._is_takeoff = True
        self._control_tower.notify(self, 'ready_to_take_off')

    def land(self):
        print(f'{self.get_name()} is landing')
        self._control_tower.notify(self, 'landed')
        self._is_landing = False

    def takeoff(self):
        print(f'{self.get_name()} is taking off')
        self._control_tower.notify(self, 'took_off')
        self._is_takeoff = False


# Usage
control_tower = ControlTower()

fligt1 = Aircraft('Flight 101', control_tower)
fligt2 = Aircraft('Flight 202', control_tower)
fligt3 = Aircraft('Flight 303', control_tower)

fligt1.request_landing()
fligt2.request_takeoff()
fligt3.request_landing()

fligt1.request_takeoff()