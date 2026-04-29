class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr= []
        def bt(options):
            if len(options) == 0:
                res.append(curr[:])
            for i in options:
                cpy = options.copy()
                cpy.remove(i)
                curr.append(nums[i])
                bt(cpy)
                curr.pop()
        bt( set([i for i in range(len(nums))]))
        return res