class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        added = set()
        def dfs(curr, ind):
            if len(curr) > len(res):
                return 
            if tuple(sorted(curr)) not in added:
                added.add(tuple(sorted(curr)))
                res.append(curr[:])
            for i in range(ind + 1, len(nums)):
                curr.append(nums[i])
                dfs(curr, i)
                curr.pop()
        dfs([], -1)
        return res
        