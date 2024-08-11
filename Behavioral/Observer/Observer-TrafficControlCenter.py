from abc import ABC, abstractmethod


# Subject(Publisher) Interface
class TrafficControl(ABC):
    @abstractmethod
    def register_traffic_light(self, traffic_light):
        pass

    @abstractmethod
    def remove_traffic_light(self, traffic_light):
        pass

    @abstractmethod
    def notify_traffic_lights(self):
        pass


# Concreate Subject(Publisher)
class TrafficControlCenter(TrafficControl):
    def __init__(self):
        self._traffic_lights = []
        self._traffic_condition = ""

    def register_traffic_light(self, traffic_light):
        self._traffic_lights.append(traffic_light)

    def remove_traffic_light(self, traffic_light):
        self._traffic_lights.remove(traffic_light)

    def notify_traffic_lights(self):
        for traffic_light in self._traffic_lights:
            traffic_light.update(self)

    @property
    def traffic_condition(self):
        return self._traffic_condition

    @traffic_condition.setter
    def traffic_condition(self, condition):
        self._traffic_condition = condition
        self.notify_traffic_lights()


# Observer Interface
class TrafficLight(ABC):

    @abstractmethod
    def update(self, traffic_control_center: TrafficControl):
        pass


# Concreate Observer
class ConcreateTrafficLight(TrafficLight):
    def __init__(self, location):
        self._location = location

    def update(self, traffic_control_center: TrafficControl):
        print(f'Traffic light at {self._location} updated to handle: {traffic_control_center.traffic_condition}')


# Create a traffic light center
traffic_control_center = TrafficControlCenter()

# Create traffic lights at different locations
traffic_light_1 = ConcreateTrafficLight('5th Avenue and Main Street')
traffic_light_2 = ConcreateTrafficLight('2nd Street and Elm Street')
traffic_light_3 = ConcreateTrafficLight('Central Park South')

# Register traffic lights with the control center
traffic_control_center.register_traffic_light(traffic_light_1)
traffic_control_center.register_traffic_light(traffic_light_2)
traffic_control_center.register_traffic_light(traffic_light_3)

# Update traffic conditions
traffic_control_center.traffic_condition = "Heavy traffic on Main Street"
traffic_control_center.traffic_condition = "Accident at Central Park South"
