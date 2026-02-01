class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        q = [(0, 0)]
        nbrs = defaultdict(lambda: defaultdict(int))
        rvrs = defaultdict(lambda: defaultdict(int))
        seen = set()
        for a, b, w in edges:
            nbrs[a][b] = w
            rvrs[b][a] = 2*w
        while q:
            for i in range(len(q)):
                dist, node = heapq.heappop(q)
                if node in seen:
                    continue
                seen.add(node)
                if node == n-1:
                    return dist
                for nbr, w in nbrs[node].items():
                    heapq.heappush(q, (dist + w, nbr))
                for nbr, w in rvrs[node].items():
                    heapq.heappush(q, (dist + w, nbr))
        return -1



            


