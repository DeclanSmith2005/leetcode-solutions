class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        used = set()
        memo = {}
        res = 0

        def dp(i, total):
            nonlocal res
            if total > amount or i == len(coins):
                return 0 
            if total == amount:
                return 1
            if (i, total) in memo:
                return memo[(i, total)]
            
            use = dp(i, total + coins[i])
            skip = dp (i+1, total)
            memo[(i, total)] = use + skip
            return use + skip
        
        return dp(0, 0)
