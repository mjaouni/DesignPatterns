from abc import ABC, abstractmethod


# State Interface/abstract class
class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, traffic_light: 'TrafficLight'):
        pass


class RedLightState(TrafficLightState):
    def handle(self, traffic_light: 'TrafficLight'):
        print('Red Light - Stop!')
        traffic_light.state = GreenLightState()


class GreenLightState(TrafficLightState):
    def handle(self, traffic_light: 'TrafficLight'):
        print('Green Light - GO!')
        traffic_light.state = YellowLightState()


class YellowLightState(TrafficLightState):
    def handle(self, traffic_light: 'TrafficLight'):
        print('Yellow Light - PREPARE TO STOP!')
        traffic_light.state = RedLightState()


class TrafficLight:
    def __init__(self, traffic_light_state: TrafficLightState):
        self.state = traffic_light_state

    def change(self):
        self.state.handle(self)


# Usage
traffic_light = TrafficLight(RedLightState())
for _ in range(6):
    traffic_light.change()
