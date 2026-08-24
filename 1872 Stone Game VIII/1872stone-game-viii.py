class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        pre = list(accumulate(stones))
        memo = {len(stones) - 1: pre[-1]}

        def dp(i):
            if i in memo: 
                return memo[i]
            curr = pre[i] - dp(i+1)
            nxt = dp(i+1)
            memo[i] = max(nxt, curr)
            return max(nxt, curr)
        return dp(1)



            

