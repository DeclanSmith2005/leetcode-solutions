class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        nums = set(nums)
        res = -1
        for i in nums:
            if counts[i] == 1:
                res = max(res, i)
        return res