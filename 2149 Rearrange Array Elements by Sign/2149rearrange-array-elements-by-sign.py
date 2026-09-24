class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos, neg = 0, 0
        res = []
        while len(res) < len(nums):
            while pos < len(nums) and nums[pos] < 0:
                pos+=1
            res.append(nums[pos])
            pos+=1
            
            while neg < len(nums) and nums[neg] > 0:
                neg +=1
            res.append(nums[neg])
            neg +=1
        return res

            