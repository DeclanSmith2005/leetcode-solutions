class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0:0}
        curr = 0
        res = 0
        for i, num in enumerate(nums):
            curr += num
            if curr - k in seen:
                res = max(res, i-seen[curr-k]+1)
            if curr not in seen:
                seen[curr] = i+1
        return res