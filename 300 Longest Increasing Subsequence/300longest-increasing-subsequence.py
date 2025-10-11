class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        greatest = 0 
        for i in range(len(nums), -1, -1):
            curr = 0
            for k in range(i+1, len(nums)):
                if nums[i] < nums[k]:
                    curr =  max(memo[k]+1, curr)
            memo[i] = max(curr, 1)
            greatest = max(curr, greatest, 1)
        return greatest



