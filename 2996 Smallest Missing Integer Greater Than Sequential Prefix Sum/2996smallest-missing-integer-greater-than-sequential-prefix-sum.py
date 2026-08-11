class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        total = nums[0]
        while i < len(nums) and nums[i] == nums[i-1]+1:
            total += nums[i]
            i +=1
        while total in set(nums):
            total += 1
        return total