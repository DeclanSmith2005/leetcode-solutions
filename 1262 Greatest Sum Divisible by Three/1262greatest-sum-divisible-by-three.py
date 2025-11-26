class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        rem = 0
        dp = [[float("-inf"), float("-inf"), float("-inf")] for i in range(len(nums)+1)]
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            for r in range(3):
                dp[i][r] = max(
                    nums[i-1] + dp[i-1][(r + nums[i-1]) % 3], 
                    dp[i-1][r]
                )
        return dp[len(nums)][0]

        

            

            