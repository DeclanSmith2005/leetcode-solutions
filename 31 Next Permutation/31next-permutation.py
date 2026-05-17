class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i != 0:
            swap = i
            for k in range(i, len(nums)):
                if nums[k] > nums[i-1] and nums[k] <= nums[swap]:
                    swap = k
            tmp = nums[i-1]
            nums[i-1] = nums[swap]
            nums[swap] = tmp
        nums[i:len(nums)] = nums[i:len(nums)][::-1]
        