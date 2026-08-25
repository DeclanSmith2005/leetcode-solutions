class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        m = 1
        while k * m in nums and k*m <= max(nums):
            m+=1
        return k *m