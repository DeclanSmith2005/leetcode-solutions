class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDif = nums[k-1] - nums[0]
        for i in range(1, len(nums) - k + 1):
            minDif = min(minDif, nums[k - 1 + i] - nums[i])
        return minDif