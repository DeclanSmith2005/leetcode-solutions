class Solution:
    def maxA(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i <= 0:
                return 0
            if i in memo:
                return memo[i]
            best = dp(i-1) + 1
            for k in range(i-2):
                best = max(best, dp(k) * ((i-k)-1))   
            memo[i] = best  
            return best      
        return dp(n)
