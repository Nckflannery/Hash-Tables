
class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0  # number of elements in the DynamicArray
        self.capacity = capacity # total amount of storage in the DynamicArray
        self.storage = [None] * capacity

    def insert(self, index, value):
        # O(n) (because we will need to shift every item after insert)
        # check if we have capacity
        if self.count >= self.capacity:
            # If not, add more capacity
            self.resize()

        # Shift over every item after index to the right by 1
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        # Add new value to the index
        self.storage[index] = value

        # Increment count
        self.count += 1

    def append(self, value):
        # O(1) (except at points of resizing)
        # Adds value to end of DynamicArray
        # Check if we have enough capacity
        if self.count >= self.capacity:
            # If not, double the resize
            self.resize()

        # Add value to the index of count
        self.storage[self.count] = value

        # Increment count
        self.count += 1

    def resize(self):
        # Double capacity
        self.capacity *= 2

        # Allovate a new storage array with double capacity
        new_storage = [None] * self.capacity

        # Copy all elements from old storage to new
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

# O(n^2)
def add_to_front(n):
    x = []
    for i in range(0, n):
        x.insert(0, n - i)
    return x

# O(n)
def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i + 1)
    return x

# O(n)
def pre_allocate(n):
    x = [None] * n
    for i in range(0, n):
        x[i] = i + 1
    return x

a = DynamicArray(2)
a.insert(0, 10)
a.insert(0, 11)
print(a.storage)
a.append(9)
a.append(8)
print(a.storage)
a.append(7)

print(a.storage)
import time

start_time = time.time()
add_to_back(100000)  # O(n)
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")
# runtime: 0.07669210433959961 seconds

start_time = time.time()
add_to_front(100000)  # O(n^2)
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")
# runtime: 56.415611743927 seconds

n = 100000          # n = 500 thousand
add_to_back(n)      # 0.0752871036529541 seconds
pre_allocate(n)     # 0.05263519287109375 seconds

n = 1000000         # n = 5 million
add_to_back(n)      # 0.72271728515625 seconds
pre_allocate(n)     # 0.5194799900054932 seconds

n = 10000000        # n = 50 million
add_to_back(n)      # 7.198451995849609 seconds
pre_allocate(n)     # 5.220464706420898 seconds

# Preallocating memory is consistently ~40% faster
