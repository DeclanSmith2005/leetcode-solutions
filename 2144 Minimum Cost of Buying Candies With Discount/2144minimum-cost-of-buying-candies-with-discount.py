class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse= True)
        res = 0
        for i in range(len(cost)):
            if (i -2)%3 == 0 and i -2 > -1:
                continue
            res += cost[i]
        return res
