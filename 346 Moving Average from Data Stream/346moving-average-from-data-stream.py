class MovingAverage:

    def __init__(self, size: int):
        self.q  = deque([])
        self.avg = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.q) < self.size:
            self.q.append(val)
            self.avg = sum(self.q) / len(self.q)
        else:
            self.avg -= (self.q.popleft() / self.size)
            self.avg += (val / self.size)
            self.q.append(val)
        return self.avg

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)