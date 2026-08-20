class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]

        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if r- l < 2:
                return 0
            best = 0
            for i in range(l+1, r):
                left = dp(l, i)
                right = dp(i , r)
                curr = nums[l] * nums[i] * nums[r]
                best = max(best, left + right + curr)
            memo[(l, r)] = best
            return best

        return dp(0, len(nums)-1)