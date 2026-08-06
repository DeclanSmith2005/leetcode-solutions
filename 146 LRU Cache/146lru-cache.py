class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # k -> last_accessed, val
        self.size = 0
        self.heap = []
        self.time = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.time+= 1
        if key not in self.cache:
            return -1
        oldTime, oldVal,  = self.cache[key]
        self.cache[key] =  self.time, oldVal
        heapq.heappush(self.heap, (self.time, key))
        return oldVal

    def put(self, key: int, value: int) -> None:
        self.time+= 1
        if len(self.cache) == self.capacity and key not in self.cache:
            self.evict()
        oldTime , oldVal  = self.cache.get(key, (None, None))
        self.cache[key] = self.time, value 
        heapq.heappush(self.heap, (self.time, key))
        self.size += 1
    
    def evict(self):
        while self.heap:
            time, key = heapq.heappop(self.heap)
            if key not in self.cache or time != self.cache[key][0]:
                continue
            self.size -= 1
            del self.cache[key]
            break


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)