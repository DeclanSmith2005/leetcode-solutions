class Solution:
    def trailingZeroes(self, n: int) -> int:
        final = 1
        while n > 0:
            final *= n
            n -=1
        res = 0
        l , r = 0, floor(log(final, 10))
        while l <= r:
            mid = l + ((r - l + 1) // 2)
            if (final%10**mid) == 0:
                res = mid       
                l = mid + 1    
            else:
                r = mid - 1    
        return res


            