class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0 
        for r in range(len(nums)):
            for l in range(r+1):
                res += len(set(nums[l:r+1]))**2
        return res