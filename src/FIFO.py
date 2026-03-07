from collections import OrderedDict

class FIFO:
    def __init__(self, capacity):

        self.capacity = capacity

        #number of misses in the cache
        self.misses = 0

        #creates the cache object that tracks order of insertion
        self.cache = OrderedDict()

    def get(self, key):

        #returns value associated to the key, returns -1 if key is not found
        #for simplicity: key = value = integer ID
        return self.cache.get(key, -1)

    def put(self, key, value):
        #Key not in cache and cache is full
        if key not in self.cache and len(self.cache) >= self.capacity:
            # removes first item in the cache
            self.cache.popitem(last=False)
            #updates miss counter
            self.misses += 1

        #adds ID into the cache
        self.cache[key] = value