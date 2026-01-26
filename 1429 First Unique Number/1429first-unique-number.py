class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counts = defaultdict(int)
        self.curr = 0
        self.q = nums
        for i in nums:
            self.counts[i] +=1

    def showFirstUnique(self) -> int:
        while True:
            if self.curr >= len(self.q):
                return -1
            if self.counts[self.q[self.curr]] == 1:
                return self.q[self.curr]
            else:
                self.curr += 1
    

    def add(self, value: int) -> None:
        self.q.append(value)
        self.counts[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)