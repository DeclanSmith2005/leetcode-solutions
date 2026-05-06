class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or timestamp < self.store[key][0][0]:
            return ""
        l, r = 0, len(self.store[key])
        while l < r:
            m = (l+r) // 2
            if self.store[key][m][0] > timestamp:
                r = m
            else:
                l = m + 1
        return self.store[key][l-1][1]

     


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)