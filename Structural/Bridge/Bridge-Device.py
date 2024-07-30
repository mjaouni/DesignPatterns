from abc import ABC, abstractmethod


# Abstraction (Device)
class Device(ABC):
    def __init__(self, control_interface):
        self.control_interface = control_interface

    @abstractmethod
    def operate(self):
        pass


# Implementor (ControlInterface)
class ControlInterface(ABC):
    @abstractmethod
    def control(self):
        pass


# Light: Device Concreate Implementation
class Light(Device):
    def operate(self):
        print(f'Operating Light Device')
        self.control_interface.control()


# Thermostat: Device Concreate Implementation
class Thermostat(Device):
    def operate(self):
        print(f'Operating Thermostat Device')
        self.control_interface.control()


# MobileAppControl Concrete Implementors
class MobileAppControl(ControlInterface):
    def control(self):
        print(f'Controlling Device via Mobile App')


# VoiceAssistantControl Concrete Implementors
class VoiceAssistantControl(ControlInterface):
    def control(self):
        print(f'Controlling Device via Voice Assistant')


# RemoteControl Concrete Implementors
class RemoteControl(ControlInterface):
    def control(self):
        print(f'Controlling Device via Remote Control')


# usage

# Create a mobile app control interface
mobile_app_control = MobileAppControl()

light = Light(mobile_app_control)
light.operate()

# Create a Voice Assistant control interface
voice_assistant_control = VoiceAssistantControl()
thermostat = Thermostat(voice_assistant_control)
thermostat.operate()

# Create a remote control interface
remote_control = RemoteControl()
light_remote = Light(remote_control)
light_remote.operate()

thermostat_mobile_app = Thermostat(mobile_app_control)
thermostat_mobile_app.operate()