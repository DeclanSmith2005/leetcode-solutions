class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        
        
        #first 
        l, r = 0 , len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] >= target:
                r = m
            else:
                l = m+1
        f = l
        # last
        l, r = 0 , len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m+1
            else:
                r = m 
        l-=1
        
        return [f, l] if 0 <= f< len(nums) and 0 <= l < len(nums) and nums[f] == target and nums[l] == target else [-1, -1]