from collections import OrderedDict

class LRUcache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    # look up self.cache, move to end, return value or -1
    def get(self, key: int):
        value = self.cache.get(key)
        if value is not None:
            self.cache.move_to_end(key, last=True)
            return value
        else:
            return -1
        
    # add to self.cache, move to end, evict if over capacity
    def put(self, key: int, value:int):
        if key in self.cache:
            del self.cache[key]
       
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        