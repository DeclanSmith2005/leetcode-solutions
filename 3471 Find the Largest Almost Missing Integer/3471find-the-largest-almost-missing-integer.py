class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        subArrayCounts = defaultdict(int)
        for i in range(len(nums)):
            subArrayCounts[nums[i]] += min(i+1, len(nums)-i, k)
        return max((key for key, val in subArrayCounts.items() if val == 1), default=-1)
            
            