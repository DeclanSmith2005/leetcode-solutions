class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        i = 0
        maxShipments = 0 
        recentMax = 0
        while i<len(weight):
            recentMax = max(recentMax, weight[i])
            if weight[i] < recentMax:
                maxShipments +=1
                recentMax = 0
            i+=1
        return maxShipments