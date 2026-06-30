class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls = [0] * len(nums)
        rs = [0] * len(nums)
        total = sum(nums)
        pre = 0 
        res = []
        for i in range(len(nums)):
            ls[i] = pre
            pre += nums[i]
            rs[i] = total - pre
        for i in range(len(nums)):
            res.append(abs(ls[i] -rs[i]))
        return res
