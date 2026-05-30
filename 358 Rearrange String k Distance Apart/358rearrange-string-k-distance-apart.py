class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        q = deque([])
        counts = defaultdict(int)
        prevInd = defaultdict(lambda : float('-inf'))
        res = []
        for i in s:
            counts[i] += 1
        heap = []
        for l, c in counts.items():
            heapq.heappush(heap, (-c, l))
        while len(q) < k and heap:
            q.append(heapq.heappop(heap))
        while heap or q:
            c, l  = q.popleft()
            if not prevInd[l] <= len(res) - k:
                return ""
            res.append(l)
            prevInd[l] = len(res) -1 
            if c < -1:
                heapq.heappush(heap, (c+1, l))
            if heap:
                q.append(heapq.heappop(heap))
        return "".join(res)

