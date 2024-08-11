from abc import ABC, abstractmethod


# Mediator interface
class SmartHomeMediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


# ConcreteMediator
class SmartHomeHub(SmartHomeMediator):
    def __init__(self):
        self._devices = {}

    def register_device(self, device):
        self._devices[device.get_name()] = device

    def notify(self, sender, event):

        if event == 'light_on':
            print(f'{sender.get_name()} turns on the light')
            self.adjust_thermostat('increase')

        elif event == 'door_unlocked':
            print(f'{sender.get_name()} unlocked the door')
            self.turn_on_lights()
            self.activate_security_camera()

        elif event == 'leave_home':
            print(f'{sender.get_name()} is leaving home')
            self.turn_off_lights()
            self.adjust_thermostat('decrease')

    def turn_on_lights(self):
        if 'Light' in self._devices:
            self._devices['Light'].turn_on()

    def turn_off_lights(self):
        if 'Light' in self._devices:
            self._devices['Light'].turn_off()

    def lock_doors(self):
        if 'DoorLock' in self._devices:
            self._devices['DoorLock'].lock()

    def adjust_thermostat(self, action):
        if 'Thermostat' in self._devices:
            if action == 'increase':
                self._devices['Thermostat'].increase_temperature()
            elif action == 'decrease':
                self._devices['Thermostat'].decrease_temperature()

    def activate_security_camera(self):
        if 'SecurityCamera' in self._devices:
            self._devices['SecurityCamera'].activate()


# Colleague classes
class SmartDevice:
    def __init__(self, name, hub):
        self._name = name
        self._hub = hub
        self._hub.register_device(self)

    def get_name(self):
        return self._name


class Light(SmartDevice):
    def turn_on(self):
        print(f'{self.get_name()} is now ON')
        self._hub.notify(self, 'light_on')

    def turn_off(self):
        print(f'{self.get_name()} is now OFF')


class DoorLock(SmartDevice):
    def unlock(self):
        print(f'{self.get_name()} is unlocked')
        self._hub.notify(self, 'door_unlocked')

    def lock(self):
        print(f'{self.get_name()} is locked')
        self._hub.notify(self, 'leave_home')


class Thermostat(SmartDevice):
    def increase_temperature(self):
        print(f'{self.get_name()} is increasing temperature')

    def decrease_temperature(self):
        print(f'{self.get_name()} is decreasing temperature')


class SecurityCamera(SmartDevice):
    def activate(self):
        print(f'{self.get_name()} is activated')


# Usage
hub = SmartHomeHub()

light = Light('Light', hub)
door_lock = DoorLock('DoorLock', hub)
thermostat = Thermostat('Thermostat', hub)
security_camera = SecurityCamera('SecurityCamera', hub)

# Simulate events
door_lock.unlock()
print('__________________________________________')
light.turn_on()
print('__________________________________________')
door_lock.lock()
