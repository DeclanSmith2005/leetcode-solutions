class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        res = []
        prev = lower
        for i in range(len(nums)):
            nxt = nums[i]
            if prev < nxt:
                res.append([prev, nxt-1])
            prev = nxt+1
        if prev <= upper:
            res.append([prev, upper])
        return res