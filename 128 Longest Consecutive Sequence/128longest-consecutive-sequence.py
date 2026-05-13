class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        if not nums:
            return 0
        for num in nums:
            count = 0
            if num - 1 in nums:
                continue
            while num +1 in nums:
                count +=1
                num+=1
            res = max(res, count)
        return res + 1
        