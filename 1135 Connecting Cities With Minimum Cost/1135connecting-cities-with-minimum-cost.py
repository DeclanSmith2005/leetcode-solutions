class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        adj = defaultdict(list) # n -> nbrs
        for a, b, c in connections:
            adj[a].append((b, c))
            adj[b].append((a, c))
        res = 0
        heap = [(0, 1)]
        seen = set()
        while heap: 
            cost, curr = heapq.heappop(heap)
            if curr in seen:
                continue
            res += cost
            seen.add(curr)
            for nbr, c in adj[curr]:
                heapq.heappush(heap, (c, nbr))
        return res if len(seen) == n else -1
        

        