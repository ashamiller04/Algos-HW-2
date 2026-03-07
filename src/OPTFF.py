from collections import OrderedDict, defaultdict

class OPTFF:

    def __init__(self, capacity, requests):

        self.capacity = int(capacity)

        self.requests = requests

        self.cache = OrderedDict()

        self.misses = 0

        self.occurrences = defaultdict(list)
        for i, request in enumerate(self.requests):
            self.occurrences[request].append(i)


    def miss(self):
        # updates miss counter
        self.misses += 1


    def get(self, key):
        # returns value associated to the key, returns -1 if key is not found
        # for simplicity: key = value = integer ID

        if key not in self.cache:
            return -1

        return self.cache[key]


    def update(self, key, value, m):
        #key not in cache and cache full
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                #finds the farthest future use and ejects it

                ejected = None
                furthest_use = -1
                for i in self.cache:
                    next = self.occurrences.get(i, -1)

                    option = m + 1 if next == -1 else next
                    if option > furthest_use:
                        furthest_use = option
                        ejected = i

                self.cache.pop(ejected)
                self.occurrences.pop(ejected, None)

        self.cache[key] = value
