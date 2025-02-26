class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # Most recently used is index 0
        self.lru = []
        # The keys in our cache
        self.cache = set()


    def refer(self, key):
        if key not in self.cache:
            while len(self.lru) >= self.capacity:
                old_key = self.lru.pop()
                self.cache.remove(old_key)
            self.cache.add(key)
            self.lru.insert(0, key)
        else:
            self.lru.remove(key)
            self.lru.insert(0, key)

    def display(self):
        for i in self.lru:
            print(i,end=' ')
        print('')
