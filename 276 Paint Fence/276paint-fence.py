class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0, 0]for i in range(n)]
        dp [0] = [k, 0]

        for i in range(1, n):
            wtp1, wtp2 = dp[i-1]
            dp[i] = [wtp1*(k-1) + wtp2*(k-1), wtp1]
        return sum(dp[-1])
        
