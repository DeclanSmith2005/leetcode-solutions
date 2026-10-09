class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr, res, l = nums[0] ,nums[0], 0
        for r in range(1, len(nums)):
            while curr < 0 and l <= r:
                curr -= nums[l]
                l+=1
            curr += nums[r]
            res = max(res, curr) if l < r else res
        return max(res, max(nums))