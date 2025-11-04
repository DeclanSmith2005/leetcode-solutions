class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0 
        lead , lag = cost[1],  cost[0]
        for i in range(2, len(cost)):
            curr = min(lead, lag) + cost[i]
            lag = lead
            lead = curr
        return min(lag, lead)
