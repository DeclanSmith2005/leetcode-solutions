class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        adj = defaultdict(list)
        heap = [(0, 0, discounts)] # cumulative cost, node, discounts remaining
        best = defaultdict(lambda : defaultdict(lambda : float('inf'))) # [city][discountsremaining] -> best cost
        best[0][discounts] = 0

        for a, b , cost in highways:
            adj[a].append((b, cost))
            adj[b].append((a, cost))
        while heap:
            cost, node, rem = heapq.heappop(heap)
            if cost > best[node][rem]:
                continue
            if node == n-1:
                break
            for nbr, nextCost in adj[node]:
                b = nextCost + cost
                if rem: 
                    a = nextCost // 2 + cost 
                    if best[nbr][rem -1] > a:
                        best [nbr][rem-1] = a
                        heapq.heappush(heap, (a, nbr, rem - 1))
                if best[nbr][rem] > b:
                    best[nbr][rem] = b
                    heapq.heappush(heap, (b, nbr, rem))
        
        if n-1 not in best:
            return -1
        return min(best[n - 1].values())            

                
