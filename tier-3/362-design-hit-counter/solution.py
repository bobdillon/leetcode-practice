from collections import deque

class HitCounter:
    def __init__(self):
        #self.timestamp = timestamp
        self.counter = deque()

    # records a hit that happened at timestamp
    def hit(self, timestamp: int):
        self.counter.append(timestamp)
    
    def getHits(self, timestamp: int):
        #remove all but last 300 timestamps
        while self.counter and self.counter[0]<=timestamp-300:
            self.counter.popleft()
        return len(self.counter)
        

HitCounter()