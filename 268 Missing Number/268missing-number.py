class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new = [0]*(len(nums)+1)
        for i in nums:
            new[i] = 1
        for i in range(len(new)):
            if new[i] != 1:
                return i
        return len(nums)

