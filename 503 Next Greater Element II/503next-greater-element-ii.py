class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # ez monotomic stack bang
        n = len(nums)
        mono = []
        nums = nums + nums
        res = [-1 for i in range(len(nums))]
        for i, num in enumerate(nums):
            while mono and num > mono[-1][1]:
                ind, val = mono.pop()
                res[ind] = num
            mono.append((i, num))
        return res[:n]
