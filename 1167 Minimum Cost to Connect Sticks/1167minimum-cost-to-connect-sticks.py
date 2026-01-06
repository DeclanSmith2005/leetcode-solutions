class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        cost = 0
        for i in sticks:
            heapq.heappush(heap, i)
        while len(heap) >1:
            temp = heapq.heappop(heap) + heapq.heappop(heap)
            cost += temp
            heapq.heappush(heap, temp)
        return cost