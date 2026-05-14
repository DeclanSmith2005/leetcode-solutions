class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        heap = []
        for s, e in intervals:
            while heap and s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            res = max(res, len(heap))
        return res
