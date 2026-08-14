class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr = 0 
        prefix = [0]* 10001
        for cost, s, e in trips:
            prefix[s] += cost
            prefix[e] -= cost
        for i in range(len(prefix)):
            curr += prefix[i]
            if curr > capacity:
                return False
        return True
