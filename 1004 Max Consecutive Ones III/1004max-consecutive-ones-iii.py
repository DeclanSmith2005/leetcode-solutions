class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            if count + k < r-l + 1:
                if nums[l] == 1:
                    count-=1
                l+= 1
            else:
                res = r-l+1
        return res
