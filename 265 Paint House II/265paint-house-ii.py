class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        memo = defaultdict(lambda: float('inf'))
        def rc (i, colour):
            if memo[(i, colour)] < float('inf'):
                return memo[(i, colour)]
            if i == len(costs):
                return 0
            for k in range(len(costs[0])):
                if k == colour:
                    continue
                memo[(i , colour)] = min(memo[(i, colour)], rc(i+1, k))
            memo[(i,colour)] += costs[i][colour]
            return memo[(i,colour)]
        return min(rc(0, k) for k in range(len(costs[0])))
            
