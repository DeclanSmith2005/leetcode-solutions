class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        nums[0:len(nums)] = ([0]*counts[0]) + ([1]*counts[1] )+ (counts[2]*[2])
