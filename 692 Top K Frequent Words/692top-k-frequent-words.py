class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        count = Counter(words)
        seen = set()

        for w in words:
            c = count[w]
            if w in seen:
                continue
            seen.add(w)
            if heap:
                leastCount, leastWord = heap[0]
            if len(heap) < k:
                heapq.heappush_max(heap, (-c, w))
                continue
            if c > -leastCount or (c ==  -leastCount and w < leastWord):
                heapq.heappop_max(heap)
                heapq.heappush_max(heap, (-c, w))

        tmp = sorted([heapq.heappop_max(heap) for _ in range(k)], key = lambda x: (x[0], x[1]))

        return [i[1] for i in tmp]



        