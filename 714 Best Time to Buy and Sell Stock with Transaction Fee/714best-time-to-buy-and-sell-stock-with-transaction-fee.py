class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """memo = {}
        def rc (ind, holding):
            temp = 0
            if ind == len(prices):
                return temp
            if (ind, holding) in memo:
                return memo[(ind, holding)]
            if not holding:
                temp = max(
                    rc(ind+1, True) - prices[ind],
                    rc(ind+1, False)
                )
            else:
                temp = max(
                    rc(ind+1, True),
                    rc(ind+1, False) + prices[ind] - fee
                )
            memo[(ind, holding)] = temp
            return temp
        return rc(0, False)"""

        dp = [[0, 0] for i in range(len(prices)+1)] # [holding, not holding]
        for i in range(len(prices)-1, -1, -1):
            dp[i][1] = max( dp[i+1][0] - prices[i], dp[i+1][1])
            dp[i][0] = max( dp[i+1][0], dp[i+1][1] + prices[i] - fee)
        return dp[0][1]