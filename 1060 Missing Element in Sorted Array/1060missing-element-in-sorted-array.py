class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # missing at index = value - startval - ind
        # looking for first case where missing at index = k -> go left by 1 -> add 1 bang
        def mai(i):
            return nums[i] - nums[0] - i

        l , r = 0, len(nums)
        while (l < r):
            m = (l + r) // 2
            if mai(m) < k:
                l = m + 1
            else:
                r = m
        return nums[l-1] + (k-mai(l-1))  
