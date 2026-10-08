class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        for i, val1 in enumerate(nums):
            seen = set()
            #if val1 not in dups:
            for j, val2 in enumerate(nums[i + 1 :]):
                complement = -val1 - val2
                if complement in seen:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen.add(val2)
        return [list(x) for x in res]