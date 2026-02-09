class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.a = deque(v1)
        self.b = deque(v2)
        self.prev = 1

    def next(self) -> int:
        print(self.prev)
        self.prev = abs(self.prev-1)
        if len(self.a) > 0 and len(self.b)>0:
            return self.a.popleft() if self.prev == 0 else self.b.popleft()
        else:
            return self.a.popleft() if len(self.a) > 0 else self.b.popleft()

    def hasNext(self) -> bool:
        return self.a or self.b

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())