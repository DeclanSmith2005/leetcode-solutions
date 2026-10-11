class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        p, rp = {-1: 0, 0 : nums[0]}, {}
        for i in range(1, len(nums)):
            p[i] = p[i-1] + nums[i]
        total = p[len(nums)-1]
        for i in range(len(nums)):
            rp[total - p[i-1]] = i

        res = float('inf')
        for i in range(len(nums)):
            rem = x - p[i]
            if rem in rp and rp[rem] > i:
                res = min(res, i + (len(nums) - rp[rem]) +1)
            if x - p[i] == 0:
                res = min(res, i+1)
        if x in rp:
            res = min(res, len(nums) - rp[x])
        return res if res < float('inf') else -1