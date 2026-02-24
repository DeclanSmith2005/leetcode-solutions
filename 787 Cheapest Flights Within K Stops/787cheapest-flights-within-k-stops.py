class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [float('inf') for i in range(n)]
        adj = defaultdict(lambda: defaultdict(int))
        for start, dest, price in flights:
            adj[start][dest] = price
        heap = [(0, src)]
        iters = 0 

        while heap and iters < k+1:
            nxt = []
            print(heap)
            for i in range(len(heap)):
                cost, node = heapq.heappop(heap)
                for nbr, price in adj[node].items():
                    if price+cost < dists[nbr]:
                        dists[nbr] = min(dists[nbr], price + cost)
                        nxt.append((price+cost, nbr))
            for tup in nxt:
                heapq.heappush(heap, tup)
            iters += 1
        
        return dists[dst] if dists[dst] < float('inf') else -1

