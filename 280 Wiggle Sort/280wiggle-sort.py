class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l, r = 0, len(nums)-1
        res = [0] * len(nums)
        if len(nums) < 2:
            return
        i=0
        while i+1 < len(nums):
            res[i] = nums[l]
            res[i+1] = nums[r]
            l, r, i= l +1, r-1, i+2
        res[-1] = nums[l]
        nums[:] = res
