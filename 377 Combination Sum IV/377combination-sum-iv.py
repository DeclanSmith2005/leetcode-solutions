class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp  = [0]*(target+1)
        dp[0] = 1
        nums = set(nums)
        for i in range(1, target+1):
            for k in range(i):
                if (i - k) in nums:
                    dp[i] += dp[k]
        return dp[-1]
           

            
