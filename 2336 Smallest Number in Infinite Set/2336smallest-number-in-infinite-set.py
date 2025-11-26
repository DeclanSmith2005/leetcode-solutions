class SmallestInfiniteSet:

    def __init__(self):
        self.currentNum = 1
        self.heap = []
        self.heapset = set()
        
    def popSmallest(self) -> int:
        if not self.heap:
            self.currentNum +=1
            return self.currentNum -1 
        else:
            curr = heapq.heappop(self.heap)
            self.heapset.remove(curr)
            return curr


    def addBack(self, num: int) -> None:
        if self.currentNum > num and num not in self.heapset:
            self.heapset.add(num)
            heapq.heappush(self.heap, num)

       


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)