class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mins = [0] * len(nums)
        maxs = [0] * len(nums)
        mins[0] = nums[0]
        maxs[-1] = nums[-1]
        for i in range(1, len(nums)):
            mins[i] = min(mins[i-1], nums[i])
        for i in range(len(nums)-2,-1, -1):
            maxs[i] = max(maxs[i+1], nums[i])
        for i in range(len(nums)):
            if mins[i] < nums[i] < maxs[i]:
                return True
        return False
