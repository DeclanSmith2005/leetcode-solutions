class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def rc(curr, ind):
            res.add(tuple(curr[:]))
            for i in range(ind, len(nums)):
                curr.append(nums[i])
                rc(curr, i+1)
                curr.pop()
        rc([], 0)
        return [list(i) for i in res]