class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(ind, rem):
            if (ind, rem) in memo: 
               return memo[(ind, rem)]
            if ind == len(nums):
                if rem == 0:
                    return 1
                else:
                    return 0
            for m in [-1, 1]:
                memo[(ind, rem)] = memo.get((ind,rem), 0) + dp(ind+1, rem - nums[ind]*m)
            return memo[ind,rem]
        return dp(0, target)
