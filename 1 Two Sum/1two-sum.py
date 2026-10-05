class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        for i, val in enumerate(nums):
            if target - val in hm:
                return hm[target-val], i
            hm[val] = i 
        return -1 