class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = res = 0
        z_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z_count += 1
            if z_count <= 1:
                res = max(res, i+1 - left)
            else:
                if nums[left] == 0:
                    z_count -= 1
                left += 1
        return res
            