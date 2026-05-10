class MaxStack:

    def __init__(self):
        self.garbage = set()
        self.maxStack = []
        self.stack = []
        self.time = 0 

    def push(self, x: int) -> None:
        heapq.heappush(self.stack, (self.time, x))
        heapq.heappush(self.maxStack, (-x, self.time))
        self.time-=1

    def pop(self) -> int:
        while self.stack and self.stack[0][0] in self.garbage:
            heapq.heappop(self.stack)
        sig, val = heapq.heappop(self.stack)
        self.garbage.add(sig)
        return val

    def top(self) -> int:
        while self.stack and self.stack[0][0] in self.garbage:
            heapq.heappop(self.stack)
        return self.stack[0][1]

    def peekMax(self) -> int:
        while self.maxStack and self.maxStack[0][1] in self.garbage:
            heapq.heappop(self.maxStack)
        return -self.maxStack[0][0]

    def popMax(self) -> int:
        while self.maxStack and self.maxStack[0][1] in self.garbage:
            heapq.heappop(self.maxStack)
        val, sig = heapq.heappop(self.maxStack)
        self.garbage.add(sig)
        return -val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()