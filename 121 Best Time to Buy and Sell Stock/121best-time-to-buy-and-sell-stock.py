class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf')
        res= 0
        for i, p in enumerate(prices):
            res = max(res, p - mini)
            mini = min(mini, p)
        return res