from collections import OrderedDict

class LRU:
    def __init__(self, capacity):

        self.capacity = capacity

        # number of misses in the cache
        self.misses = 0

        # creates the cache object that tracks order of insertion
        self.cache = OrderedDict()


    def miss(self):
        # updates miss counter
        self.misses += 1


    def get(self, key):

        # returns value associated to the key, returns -1 if key is not found
        # for simplicity: key = value = integer ID
        if key not in self.cache:

            return -1

        #if key is found, moves it to end to indicate recent use
        self.cache.move_to_end(key)

        return self.cache[key]


    def put(self, key, value):

        #moves key to end to indicate recent use
        if key in self.cache:
            self.cache.move_to_end(key)

        #add or update key in cache
        self.cache[key] = value

        #if cache is full, removes least frequently used item
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)