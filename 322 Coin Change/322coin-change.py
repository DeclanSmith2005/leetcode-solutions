from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(remaining):
            if remaining <= 0:
                if remaining == 0:
                    memo[amount] = 0
                    return 0
                return float('inf')
            if remaining in memo:
                return memo[remaining]
            memo[remaining] = min(1 + dp(remaining- c) for c in coins)
            return memo[remaining]
        res = dp(amount)
        return res if res < float('inf') else -1
             
