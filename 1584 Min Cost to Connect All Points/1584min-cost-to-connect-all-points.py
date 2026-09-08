class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res= 0
        seen = set([0])
        heap = []
        curr = 0 

        while len(seen) < len(points):
            a, b = points[curr]
            for k, (x, y) in enumerate(points):
                if k not in seen and curr != k:
                    heapq.heappush(heap, (abs(a-x) + abs(b-y), k))
            while heap and heap[0][1] in seen:
                heapq.heappop(heap)
            cost, nxt = heapq.heappop(heap)
            seen.add(nxt)
            res+= cost
            curr = nxt
        return res
