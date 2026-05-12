class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pick the smallest k that satisfies eating everything under h hrs
        # binary search on k ? 
        def check(k: int) -> bool:
            total = 0 
            if k == 0:
                return 0 
            for pile in piles:
                if pile % k == 0:
                    total += pile // k
                else:
                    total+= (pile//k) + 1
            return total <= h
        
        l, r = (sum(piles) // h), max(piles)
        while l < r:
            m = (l+r)//2
            if check(m):
                r = m 
            else:
                l = m+1
        return l


