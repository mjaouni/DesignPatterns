from abc import ABC, abstractmethod


# Abstract Class
class ExpensiveComputation(ABC):
    @abstractmethod
    def compute(self, x):
        pass


class RealExpensiveComputation(ExpensiveComputation):

    def compute(self, x):
        # Simulate expensive computation
        print(f'Performing expensive computation of {x}')

        return x ** x


# Proxy Class
class CachingProxyExtensiveComputation(ExpensiveComputation):
    def __init__(self):
        self.real_computation = RealExpensiveComputation()
        self.cache = {}

    def compute(self, x):
        if x not in self.cache:
            print(f'Cache miss for {x}.Computing and storing in cache')
            self.cache[x] = self.real_computation.compute(x)
        else:
            print(f'Cache hit for {x}.Retrieving from cache')
        return self.cache[x]


# Usage

# First call, cache miss
proxy_computation = CachingProxyExtensiveComputation()
result1 = proxy_computation.compute(4)
print(f'Result:{result1}')

# Second call, cache hit
result2 = proxy_computation.compute(4)
print(f'Result:{result2}')

# Another call with different input, cache miss
result3 = proxy_computation.compute(10)
print(f'Result:{result3}')

# Call with the first input again, cache hit
result4 = proxy_computation.compute(4)
print(f'Result:{result4}')
