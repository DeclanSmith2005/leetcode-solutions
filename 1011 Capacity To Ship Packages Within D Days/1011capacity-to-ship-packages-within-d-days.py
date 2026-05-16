class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # similar to koko eating bannanas binary search? 
        def check(cap):
            days_used = 1
            curr = 0
            for w in weights:
                if w > cap:
                    return False
                if curr + w > cap:
                    days_used += 1
                    curr = 0
                curr += w
            return days_used <= days

        l, r = 1, sum(weights)
        while l < r:
            m = (l+r)//2
            if check(m):
                r = m
            else:
                l = m + 1
        return l

