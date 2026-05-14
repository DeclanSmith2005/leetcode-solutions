class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # need monotonic behavhiour for a sliding window generally speaking!!!
        prefix = 0 
        counts = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            counts[prefix] += 1
            prefix += nums[i]
            res += counts[prefix-k]
        return res

