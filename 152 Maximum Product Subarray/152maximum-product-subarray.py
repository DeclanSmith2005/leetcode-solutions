class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, pos, neg = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            if nums[i] == 0:
                pos = neg = 1
                res = max(res, 0) 
            else:
                tmp1, tmp2 = neg * nums[i], pos*nums[i]
                neg = min(tmp1, tmp2, nums[i])
                pos = max(tmp1, tmp2, nums[i])
                res = max(res, pos)
        return res
