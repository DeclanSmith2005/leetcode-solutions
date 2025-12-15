class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        def rc (i, colour):
            if (i, colour) in memo:
                return memo[(i, colour)]
            if i == len(costs):
                return 0
            memo[(i,colour)]=min(rc(i+1,(colour+1)%3), rc(i+1,(colour+2)%3)) + costs[i][colour]
            return memo[(i,colour)] 
        return min(rc(0, 0), rc (0, 1), rc(0,2))
            