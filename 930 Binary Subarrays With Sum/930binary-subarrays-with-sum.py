class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        l, r = 0, 0
        res = 0
        p = defaultdict(int)
        total = nums[0]

        for i in range(len(nums)):
            p[total] += 1
            total += nums[i]
            if total - goal in p:
                res+= p[total - goal]

        return res

