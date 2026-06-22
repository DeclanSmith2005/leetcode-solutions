class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, canBuy):
            if i >= len(prices):
                return 0
            ans = dp(i+1, canBuy)  # Skip
            if canBuy:
                ans = max(ans, dp(i+1, False) - prices[i])  # Buy
            else:
                ans = max(ans, dp(i+2, True) + prices[i])  # Sell
            return ans
                
        return dp(0, True)