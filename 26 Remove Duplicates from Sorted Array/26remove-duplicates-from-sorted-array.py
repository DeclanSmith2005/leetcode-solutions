class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        u = 0
        for i in range(len(nums)):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                nums[u] = nums[i]
                u+=1
        return u
