class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr, used = [], set()
        nums.sort()
        def bt(ind):
            nonlocal res
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if i in used or (i > 0 and nums[i] == nums[i-1] and (i-1) not in used):
                    continue
                used.add(i)
                curr.append(nums[i])
                bt(ind+1)
                curr.pop()
                used.remove(i)
        bt(0)
        return res        



            