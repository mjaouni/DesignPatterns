from abc import ABC, abstractmethod


class Service(ABC):

    @abstractmethod
    def request(self):
        pass


# Real Remote Service
class RealService(Service):

    def request(self):
        return 'Response from remote service'


# Proxy of Remote Service
class RemoteServiceProxy(Service):

    def __init__(self):
        self.real_service = RealService()

    def request(self):
        print('Making a request to the remote service...')
        return self.real_service.request()


# Usage
proxy_service = RemoteServiceProxy()
print(proxy_service.request())
