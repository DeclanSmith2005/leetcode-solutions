class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        ans = [-1 for i in range(len(workers))]
        heap = []
        workerBikesPreferences = [[] for _ in range(len(workers))]
        usedw, usedb = set(), set()

        for w in range(len(workers)):
            wx, wy = workers[w]
            for b in range(len(bikes)):
                bx, by = bikes[b]
                workerBikesPreferences[w].append((abs(wx-bx)+ abs(wy-by),w,b))
            workerBikesPreferences[w].sort(reverse= True)
            heapq.heappush(heap, workerBikesPreferences[w].pop())
        
        while heap:
            dist, w, b = heapq.heappop(heap)
            if not (w in usedw or b in usedb):
                ans[w] = b
                usedw.add(w)
                usedb.add(b)
            else:
                heapq.heappush(heap, workerBikesPreferences[w].pop())
        return ans