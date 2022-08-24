"""
Hashing : Open Addressing
In open addressing, we have fixed number of slots N and 
N >= number of keys ( m ) 

We just have to find an empty slot for a given key by running an iteration of hash functions and slots till getting a FREE slot.


In case of not finding a free space, flag/raise an error.

"""

import math
from abc import abstractmethod


# Hash functions
class hash_fn:
    def __init__(self, size):
        self.size = size

    def simple(self, key):
        return key % self.size

    def simple_x(self, key):
        return 1 + (key % self.size)

    def multiply(self, key):
        factor = 0.15
        return math.floor(self.size * ((key * factor) % 1))


# Core Hash Table
class hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.fn = hash_fn(self.size)

    @abstractmethod
    def get_empty_slot(self, key):
        pass

    @abstractmethod
    def get_matching_slot(self, key):
        pass

    def get(self, key):
        slot = self.get_matching_slot(key)
        if self.table[slot] == key:
            return self.table[slot]
        return None

    def insert(self, key):
        slot = self.get_empty_slot(key)
        if self.table[slot] == None:  # Free slot
            self.table[slot] = key
        else:  # It means, we did not get any free slots
            raise Exception(
                "Sorry we are unable to insert the value. Table is full")

    def remove(self, key):
        slot = self.get_matching_slot(key)
        if self.table[slot] == key:
            # We cannot set None because it will cause search disruption
            # for next entries
            self.table[slot] = "deleted"
        else:
            raise Exception("Cannot delete the key. No matching key found. ")


# Hash Table implementation with linear probe
# In linear probe, we increment the iteration by 1
class linear_hash_table(hash_table):
    def __init__(self, size):
        super().__init__(size)

    def get_empty_slot(self, key):
        # Run a simple hash query and get a slot
        # In linear probe we just use single hash function of choice
        slot = self.fn.simple(key)
        # Ideally it should be 0 but we have already run a hash query in above line
        iteration = 1
        while self.table[slot] is not None and iteration <= self.size:
            # Increment is 1, which tells us it is linear probe
            increment = 1
            # We are just incrementing slot by 1 and applying divide logic again
            slot = (slot + increment) % self.size
            # Increase the iteration count
            iteration = iteration + 1
        return slot

    def get_matching_slot(self, key):
        # Run a simple hash query and get a slot
        # In linear probe we just use single hash function of choice
        slot = self.fn.simple(key)
        # Ideally it should be 0 but we have already run a hash query in above line
        iteration = 1
        while self.table[slot] != key and iteration <= self.size:
            # Increment is 1, which tells us it is linear probe
            increment = 1
            # We are just incrementing slot by 1 and applying divide logic again
            slot = (slot + increment) % self.size
            # Increase the iteration count
            iteration = iteration + 1
        return slot


# Hash Table implementation with quadratic probe
# In linear probe, we increment the iteration by iteration * iteration
class quadratic_hash_table(hash_table):
    def __init__(self, size):
        super().__init__(size)

    def get_empty_slot(self, key):
        # Run a simple hash query and get a slot
        # In quadratic probe we just use single hash function of choice
        slot = self.fn.simple(key)
        # Ideally it should be 0 but we have already run a hash query in above line
        iteration = 1
        while self.table[slot] is not None and iteration <= self.size:
            # Increment is iteration ^ 2, which tells us it is quadratic probe
            increment = iteration * iteration
            # We are just incrementing slot by iteration ^ 2 and
            # applying divide logic again
            slot = (slot + increment) % self.size
            # Increase the iteration count
            iteration = iteration + 1
        return slot

    def get_matching_slot(self, key):
        # Run a simple hash query and get a slot
        # In linear probe we just use single hash function of choice
        slot = self.fn.simple(key)
        # Ideally it should be 0 but we have already run a hash query in above line
        iteration = 1
        while self.table[slot] != key and iteration <= self.size:
            # Increment is iteration ^ 2, which tells us it is quadratic probe
            increment = iteration * iteration
            # We are just incrementing slot by iteration ^ 2 and
            # applying divide logic again
            slot = (slot + increment) % self.size
            # Increase the iteration count
            iteration = iteration + 1
        return slot


# Hash Table implementation with double hash probe
# In double hash probe, we increment the iteration by iteration * hash_fn2()
class double_hash_table(hash_table):
    def __init__(self, size):
        super().__init__(size)

    def get_empty_slot(self, key):
        # Run a simple hash query and get a slot
        # In quadratic probe we just use single hash function of choice
        slot = self.fn.simple(key)
        # Ideally it should be 0 but we have already run a hash query in above line
        iteration = 1
        while self.table[slot] is not None and iteration <= self.size:
            # Increment is iteration * second_hash_fn, which is double hashing
            increment = iteration * self.fn.multiply(key)
            # We are just incrementing slot by iteration ^ 2 and
            # applying divide logic again
            slot = (slot + increment) % self.size
            # Increase the iteration count
            iteration = iteration + 1
        return slot

    def get_matching_slot(self, key):
        # Run a simple hash query and get a slot
        # In linear probe we just use single hash function of choice
        slot = self.fn.simple(key)
        # Ideally it should be 0 but we have already run a hash query in above line
        iteration = 1
        while self.table[slot] != key and iteration <= self.size:
            # Increment is iteration * second_hash_fn, which is double hashing
            increment = iteration * self.fn.multiply(key)
            # We are just incrementing slot by iteration ^ 2 and
            # applying divide logic again
            slot = (slot + increment) % self.size
            # Increase the iteration count
            iteration = iteration + 1
        return slot
