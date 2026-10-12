class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        zeroCount = 0 
        for i, v in enumerate(nums):
            if v != 0:
                nums[l] = v
                l += 1
            else:
                zeroCount += 1
        for i in range(len(nums)- zeroCount, len(nums)):
            nums[i] = 0
        