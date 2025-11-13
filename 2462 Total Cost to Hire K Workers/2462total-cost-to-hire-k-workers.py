class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        res = 0
        l , r = 0, len(costs)-1
        lmax = rmax = candidates
        while k > 0:
            while len(costs)-1 - r < rmax and l <= r:
                heapq.heappush(heap, (costs[r], r))
                r-=1
            while l < lmax and l <= r:
                heapq.heappush(heap, (costs[l], l))
                l+=1
            temp = heapq.heappop(heap)
            res += temp [0]
            if 0 <= temp[1] <= l:
                lmax+=1
            else:
                rmax+=1
            k-=1
        return res

