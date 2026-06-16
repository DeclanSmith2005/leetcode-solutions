class Logger:

    def __init__(self):
        self.coolDown = set()
        self.q = deque([])

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and self.q[0][0] <= timestamp - 10:
            self.coolDown.remove(self.q.popleft()[1])
        if message not in self.coolDown:
            self.q.append((timestamp, message))
            self.coolDown.add(message)
            return True
        return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)