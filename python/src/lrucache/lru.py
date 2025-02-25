class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # Least recently used is index 0
        self.lru = []
        # The keys in our cache
        self.cache = set()


    def refer(self, key):
        if key not in self.cache:
            while len(self.lru) >= self.capacity:
                old_key = self.lru.pop(0)
                self.cache.remove(old_key)
            # Don't use the stored value
            self.cache.add(key)
        else:
            # Possible O(n) step
            self.lru.remove(key)
        # update reference
        self.lru.append(key)

    def display(self):
        for i in self.lru:
            print(i,end=' ')
        print('')
