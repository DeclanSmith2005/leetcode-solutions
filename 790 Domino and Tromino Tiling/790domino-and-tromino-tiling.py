class Solution:
    def numTilings(self, n: int) -> int:
        base = [1, 2]
        if n <=2:
            return n 
        dp = base + [0]*(n-2)
        tri = [0, 1] + [0]*(n-2)
        for i in range(2, n):
            tri[i] = (tri[i-1] + dp[i-2]) % (10**9 + 7)
            dp[i] = (dp[i-1] + dp[i-2] + 2*tri[i-1]) % (10**9 + 7)
        return dp[n-1]