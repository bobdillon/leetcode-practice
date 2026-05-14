from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    """ return value of key if it exists, else return -1"""
    def get(self, key:int):
        if key in self.cache:
            self.cache.move_to_end(key) # added by claude
            return self.cache[key]
        else:
            return -1

    """ update key value if it exists, otherwise, add kv pair to cache"""
    def put(self, key:int, value:int):
        if key in self.cache:
            #self.cache[key] = value
            del self.cache[key]
        #else:
        self.cache[key] = value

        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)




