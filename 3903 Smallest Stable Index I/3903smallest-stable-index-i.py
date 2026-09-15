class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi = nums[0]
        minis = [nums[-1]] * len(nums) 
        for i in range(len(nums)-2, -1, -1):
            minis[i] = min(minis[i+1], nums[i])
        for i in range(len(nums)):
            maxi = max(maxi, nums[i])
            if maxi - minis[i] <= k:
                return i            
        return -1