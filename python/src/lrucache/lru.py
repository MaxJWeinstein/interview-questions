class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # DLL of keys, in order of recent reference
        self.cache = []
        # For now, just a set
        self.lru = {}
        # self.lru has to be indexed by keys for fast search


    def refer(self, key):
        if key not in self.lru:
            if len(self.cache) >= self.capacity:
                old_key = self.cache.pop(0)
                del self.lru[old_key]
            # Don't use the stored value
            self.lru[key] = True
        else:
            # Possible O(n) step
            self.cache.remove(key)
        # update reference
        # Note: MRU goes at the end
        self.cache.append(key)

    def display(self):
        for i in self.cache:
            print(i,end=' ')
        print('')
